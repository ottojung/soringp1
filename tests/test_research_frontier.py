"""Frontier tests: durable exactly-once questions, no quotas, honest results."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('frontier',ROOT/'scripts/research_frontier.py')
F=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F)

class FrontierTests(unittest.TestCase):
    def sample(self):
        return json.loads((ROOT/'docs/research-frontier.json').read_text())['fronts']

    def test_seed_has_independent_specific_falsifiable_questions(self):
        entries=self.sample()
        self.assertGreaterEqual(len(entries),4)
        self.assertEqual(len({x['id'] for x in entries}),len(entries))
        for x in entries:self.assertTrue(F.valid(x),x)

    def test_duplicate_proposals_rejected_without_claiming_theorems(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/'frontier.json'
            existing=[dict(self.sample()[0],status='investigated')]
            d={'version':1,'fronts':existing,
               'curator':{'agent_id':'curator123'}}
            f=Path(temp)/'curator'/'frontier-candidates.json'
            f.parent.mkdir();f.write_text(json.dumps({'fronts':[
                self.sample()[0],
                dict(self.sample()[1],id='distinct-curated-front'),
            ]}))
            with (mock.patch.object(F,'STATE',p),mock.patch.object(F,'WORK',Path(temp)),
                  mock.patch.object(F,'status',return_value='succeeded')):
                F.curate_done(d,set())
                self.assertEqual(len(d['fronts']),2)
                self.assertEqual(d['fronts'][1]['origin'],'ai_proposal_unverified')
                self.assertEqual(d['curator']['added'],1)

    def test_entire_ready_frontier_dispatched_no_fixed_slots(self):
        d={'version':1,'fronts':[dict(x,status='ready') for x in self.sample()],
           'curator':{}}
        seen=[]
        def fake(d,row):
            seen.append(row['id']);row['status']='running'
        with (mock.patch.object(F,'live',return_value=set()),
              mock.patch.object(F,'dispatch',side_effect=fake),
              mock.patch.object(F,'save')):
            F.tick(d)
        self.assertEqual(set(seen),{x['id'] for x in self.sample()})

    def test_exhaustion_commissions_curator_not_filler(self):
        d={'version':1,'fronts':[dict(x,status='investigated') for x in self.sample()],
           'curator':{}}
        with (mock.patch.object(F,'live',return_value=set()),
              mock.patch.object(F,'curate') as curator,
              mock.patch.object(F,'save')):
            F.tick(d)
            curator.assert_called_once()

    def test_interrupted_launch_returns_to_ready(self):
        d={'version':1,'fronts':[dict(self.sample()[0],status='launching',agent_id='reserved')],
           'curator':{}}
        with mock.patch.object(F,'status',return_value='idle'):
            F.reconcile(d,set())
        self.assertEqual(d['fronts'][0]['status'],'ready')

    def test_successful_run_means_investigation_not_theorem(self):
        d={'version':1,'fronts':[dict(self.sample()[0],status='running',agent_id='agent123')],
           'curator':{}}
        with (mock.patch.object(F,'status',return_value='succeeded'),
              mock.patch.object(F,'excerpt',return_value='no conclusive proof')):
            F.reconcile(d,set())
        row=d['fronts'][0]
        self.assertEqual(row['status'],'investigated')
        self.assertIn('unverified',next(k for k in row if k=='finding_unverified'))

if __name__=='__main__':unittest.main()
