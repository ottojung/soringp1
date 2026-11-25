import Lake
open Lake DSL

package «soringp1» where
  leanOptions := #[⟨`autoImplicit, false⟩]

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.34.0"

@[default_target]
lean_lib SoringP1 where
  globs := #[.andSubmodules `SoringP1]
