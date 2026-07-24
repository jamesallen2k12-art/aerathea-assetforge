# Step 13 Technical-Fail Diagnostic Render A01 Output Record

- Date: `2026-07-24`
- Run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Diagnostic result: `PASS`
- Diagnostic artifact status: `proof only`
- Step 13 asset result: `FAIL / BLOCKED` remains unchanged
- Repair or rebuild performed: `false`
- Mirror-and-weld performed: `false`
- Blender sources saved or changed: `false`
- Final boards opened visibly: `true`
- Next state: `waiting for Flamestrike feedback`

## Plain-English Result

One diagnostic board was completed for each hammer. Each board shows the normal
model beside the exact same camera view with faulty saved joins highlighted.

The normal views can look solid because many separate panels overlap or touch.
The colored views expose that those panels are not cleanly joined:

- red marks saved panel edges with no exact matching partner;
- yellow marks saved edges used by more than two panels; and
- magenta marks directly observed reversed face winding in the local C04
  closure.

These boards explain the current problem. They do not approve a solution and
do not authorize repair, rebuilding, mirroring, welding, Step 14, export, or
Unreal work.

## Final Review Boards

### Siege Breaker

- Path: `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/review/STEP_13_TECHNICAL_FAIL_DIAGNOSTIC_A01/SM_DRW_SiegeBreaker_Hammer_A01_TECHNICAL_FAIL_DIAGNOSTIC_A01.png`
- SHA-256: `c8f45a752476076217b259046b4da3609d1ad7c333f097b388cba31cd8b738fd`
- Size: `1580 × 1280 px`
- Unpaired exact panel edges: `19,200`
- Overloaded exact edges: `890`
- Local C04 reversed-winding edges: `276 total`, or `138 on each side`
- Artifact status: `proof only; technical-failure diagnostic`

### Foe Hammer

- Path: `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/review/STEP_13_TECHNICAL_FAIL_DIAGNOSTIC_A01/SM_DRW_FoeHammer_Hammer_A01_TECHNICAL_FAIL_DIAGNOSTIC_A01.png`
- SHA-256: `71d93a8f292a9cf135b56943bd551b5032814add23a74c17e332e982527e7f5d`
- Size: `1580 × 1280 px`
- Unpaired exact panel edges: `18,900`
- Overloaded exact edges: `890`
- Local C04 reversed-winding edges: `236 total`, or `118 on each side`
- Artifact status: `proof only; technical-failure diagnostic`

Both final boards passed the internal presentation check: the complete hammer is
visible, both panels use the same camera, the color key is readable, and no
information block hides geometry.

## Technical Evidence

- Manifest: `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/STEP_13_TECHNICAL_FAIL_DIAGNOSTIC_RENDER_A01.json`
- Manifest SHA-256: `26b228c76526f5b846281bd432f6baa13ce66709d5d386932654c8ad2e0d688f`
- Renderer: `Tools/DCC/render_siegebreaker_foehammer_step13_failure_diagnostic_a01.py`
- Renderer SHA-256: `f2dce52af3b0afe13a32ab069e6dc82e1883a50675f77a86c993d104d2a14d4e`
- Approval record SHA-256: `8e7e63b621c91f855c3006ef2cb40447a397463729f5725f299703ec382d32a1`
- Manifest result: `PASS`
- Manifest assumptions: `none`
- Source-save operator invoked: `false`
- Temporary overlay curves saved to either source: `false`
- Geometry modified: `false`

## Source Integrity

### Siege Breaker

- Source SHA-256 before:
  `c69b415ac3429091c6aa77d24ffcd6d88bbd0f9fc711e3862c2c7e7b51034537`
- Source SHA-256 after:
  `c69b415ac3429091c6aa77d24ffcd6d88bbd0f9fc711e3862c2c7e7b51034537`
- Byte-identical: `true`

### Foe Hammer

- Source SHA-256 before:
  `67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4`
- Source SHA-256 after:
  `67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4`
- Byte-identical: `true`

## Rejected First Framing

The first presentation pass was internally rejected because its lower
information blocks hid part of the pommel and its legend was cramped. It was
preserved at:

`docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/review/STEP_13_TECHNICAL_FAIL_DIAGNOSTIC_A01_REJECTED_FRAMING_A01/`

Its artifact status is `rejected / proof only`; it is not a review candidate.

## Required Stop

The approved diagnostic step is complete. Production remains stopped for
Flamestrike's visual feedback and any additional data. A mirror-and-weld
rebuild, or any other recovery implementation, requires a separate explicit
step contract and approval.
