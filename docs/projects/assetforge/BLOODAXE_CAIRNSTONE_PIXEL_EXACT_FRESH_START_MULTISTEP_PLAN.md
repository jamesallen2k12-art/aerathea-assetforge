# BloodAxe Cairn Stone Pixel-Exact Fresh-Start Multi-Step Plan

Status: approved process authority

Date: 2026-07-15

Artifact classification: authoritative

This document is the approved process authority for the fresh-start project.
It authorizes the process structure only. It does not authorize measurement,
cropping, masking, interpretation, geometry, texture production, Blender work,
FBX export, Unreal work, quarantine, recovery, reclassification, commit, or
push outside a separately approved step contract.

## 1. Approval Scope

Flamestrike approved this plan on 2026-07-15.

The approval covers:

- the fresh-start authority boundary;
- the proposed 21-step sequence;
- the exact-data and interpretation separation;
- the one-complete-step-per-agent-session rule;
- the checkpoint, save, handoff, restart, commit, and push protocol;
- the 200k warning, 220k handoff reserve, and 240k mandatory stop controls;
- the final definition of pipeline completion as Approved library asset;
- the requirement for a new asset revision ID and namespace.

The exact asset revision ID remains a Step 01 decision. Approval of this plan
does not authorize Step 01 or any later production step. Each step must begin
with its own visible step contract.

## 2. Controlling Truths

### Project Goal

Create one faithful, production-ready BloodAxe Cairn Stone from the confirmed
2D multiview source, then advance it through DCC, Unreal import, validation,
performance review, Flamestrike visual approval, and approved asset-library
classification.

The asset must be a coherent 360-degree game object. It must not be a front-only
illusion, detached projection shell, procedural placeholder, approximate AI
mesh, or old-output reconstruction.

### Confirmed Source Image

Authoritative source candidate confirmed by Flamestrike in the visible review
window:

docs/assets/reference/bloodaxe_cairnstone_asset/
REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png

Source properties:

- image size: 1055 x 1491 pixels;
- format: 8-bit RGB PNG;
- source file SHA256:
  4b953abb87f5f254a5f51c6214e76d3f72c4fc55bc2fa4e4d605b2440d6e53c2;
- visible views: perspective, front, back, left, right, and top;
- declared overall height: 220 cm;
- declared monolith maximum width: 120 cm;
- declared monolith maximum depth: 90 cm;
- declared base footprint: 140 cm x 110 cm;
- declared authored base height: 35 cm.

### Exact Scanline Evidence

Manifest:

docs/assets/reference/bloodaxe_cairnstone_asset/ScanlineCapture/
REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate_ScanlineManifest.json

Existing proof:

- pixel_exact: true;
- changed_pixels: 0;
- max_rgb_delta: 0;
- target and rebuilt pixel hashes match;
- pixel SHA256:
  65b69c9674d6644fcae6795df01bdab55e59fc0c493a501ed7ed1baa966a3a72.

The source image and its verified scanline record are the only proposed
asset-specific data inputs at fresh-start initialization.

### Governing Authorities

Read and apply in this order:

1. AGENTS.md Core Principles.
2. This plan after Flamestrike approves it.
3. The approved fresh-start project charter.
4. The approved source lock and scanline manifest.
5. docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md.
6. docs/assets/CONCEPT_ART_TO_GAME_READY_ASSET_PIPELINE.md.
7. The current step contract.
8. Approved manifests and output records from completed fresh-start steps.
9. General Unreal, DCC, performance, and naming rules that do not introduce
   asset-specific legacy data.

If two authorities conflict, stop and report the conflict. Do not choose
silently.

## 3. Fresh-Start Data Firewall

### Allowed Asset-Specific Inputs

- the confirmed A02 PNG;
- its exact scanline target, scan record, rebuild, difference image, and
  manifest;
- exact integer pixel coordinates derived during approved fresh-start steps;
- source-authored dimension labels and dimension endpoints;
- fresh formulas declared and approved during this project;
- fresh manifests produced and approved during this project;
- explicit Flamestrike decisions made at named gates in this project.

### Allowed General Process Inputs

- Core;
- the generic AetherForge measurement and validation rules;
- the formal game-ready pipeline;
- generic naming, LOD, collision, UV, material, export, Unreal, and performance
  rules;
- generic validators that contain no Cairn Stone constants, crops, masks,
  component dimensions, geometry, or source-derived assets.

### Blocked Asset-Specific Inputs

- all A001, A002, A003, and A004 generated meshes;
- all A001, A002, A003, and A004 crop coordinates, masks, formulas, centers,
  measurements, component IDs, anchors, textures, UVs, normals, materials,
  LODs, collision, exports, Unreal assets, and review renders;
- old generated scripts as implementation templates;
- old manifests as source authority;
- old proof boards as visual fitting references;
- old procedural primitives or analytic footprints;
- remembered dimensions or component counts not re-derived from A02;
- visual judgment used in place of source measurement;
- outside web references, concept variants, or other Cairn Stone images;
- legacy outputs relabeled as fresh work.

Legacy records may remain preserved as quarantined history. They must not be
opened or read by a fresh-step agent unless a new Core block requires a
specifically approved historical audit. Historical lessons already promoted
into general Core or AetherForge rules remain usable as general process rules.

### Script Isolation

Fresh asset scripts must:

- use the new approved project namespace;
- declare every asset-specific constant in a fresh manifest;
- avoid imports from old Cairn Stone builders;
- avoid reading old Cairn Stone output directories;
- support non-mutating schema or preflight validation before any output path is
  opened;
- make schema-only mode incapable of producing files;
- list every input and output path before execution;
- fail closed when an input, formula, hash, or approval record is missing.

## 4. Evidence And Interpretation Boundary

### Exact Evidence

The following can be exact when properly recorded:

- source RGB pixels;
- image dimensions;
- source file and pixel hashes;
- integer pixel coordinates;
- lossless crop coordinates;
- source-authored dimension text and dimension endpoints;
- declared pixel-span convention;
- per-view pixel spans;
- per-view centimeters-per-pixel formulas;
- source-owned visible contours;
- source-owned visible centers when derived by an approved formula;
- visible contact lines;
- visible orientation marks;
- source-owned Base Color pixels;
- deterministic audit results.

### Not Exact From The Image Alone

The source does not directly and completely encode:

- the bottom surface;
- fully occluded surfaces;
- hidden component interfaces;
- internal topology;
- source-invisible thickness transitions;
- a guaranteed one-to-one cross-view correspondence for every pixel;
- surface normals;
- roughness;
- metallic values;
- ambient occlusion;
- collision;
- LOD topology;
- UV seams;
- pivot behavior;
- Unreal material behavior;
- runtime performance settings.

These items cannot be called source-derived exact data merely because they are
plausible. Each must be either:

- unnecessary and omitted;
- tagged as a blocked unknown;
- derived from an explicit general technical rule that does not alter visible
  source authority; or
- introduced through a named interpretation contract approved by Flamestrike.

### Hard Rule

No interpretation may enter an exact measurement manifest.

No exact measurement review may show a filled candidate shape, smoothed
envelope, guessed hidden surface, procedural substitute, or geometry preview.

Exact evidence and approved interpretation must remain separate in files,
manifests, review boards, and artifact-status labels.

## 5. Pixel Measurement Method

Every source view must declare its own calibration.

For an approved source span:

centimeters_per_pixel = declared_real_span_cm / measured_source_span_px

For an approved feature span:

feature_cm = feature_span_px * centimeters_per_pixel

Required controls:

- declare inclusive, exclusive, center-to-center, or edge-to-edge convention
  before measuring;
- use one convention within a pass;
- preserve full-source integer coordinates;
- record crop-local coordinates only as derived convenience values;
- do not reuse one view's calibration for another view without explicit
  authority;
- do not average conflicting views;
- do not use a bounding-box center as the physical center of an irregular
  component;
- exclude labels, arrows, gridlines, borders, and dimension marks from
  geometry ownership;
- use formula-linked source-owned contours or footprints for alignment;
- record visible, occluded, inferred, and blocked sectors separately;
- stop when source views disagree beyond declared tolerance.

The 35 cm base-height label may calibrate the authored overall base span. It
does not authorize collapsing multiple visible layers or contact lines into
one 35 cm component.

The perspective panel is visual corroboration by default. It is not metric
authority unless a fresh approved calibration contract proves that use.

## 6. Definition Of Pipeline Completion

The pipeline is complete only when the asset is an Approved library asset under
the formal status vocabulary.

Required final state:

- approved source lock;
- approved exact measurement dataset;
- approved interpretation records for every unavoidable unknown;
- DCC source candidate built and reviewed;
- DCC game-ready candidate with source, FBX, UVs, texture/material package,
  LOD0-LOD3, collision proxy, scale, pivot, and proof renders;
- Unreal import candidate with materials, textures, LODs, collision, and review
  placement configured;
- gameplay or approved review-map validation;
- performance validation;
- final Flamestrike aesthetic approval;
- approved library classification;
- complete provenance and final handoff record.

A resemblance pass, successful Blender render, valid FBX, or successful Unreal
import is not pipeline completion by itself.

## 7. Project Record Layout

Step 01 must lock the final asset ID before creating the project root.

Proposed tracked authority layout:

docs/assets/blueprints/{ASSET_ID}/

Required root records:

- {ASSET_ID}_PROJECT_CHARTER.md
- {ASSET_ID}_FRESH_START_DATA_FIREWALL.md
- {ASSET_ID}_RESET_RESUME_STATE.md
- {ASSET_ID}_ARTIFACT_INDEX.md
- {ASSET_ID}_APPROVAL_LOG.md
- steps/
- manifests/
- handoffs/

Required source/output layout after relevant approval:

- source reference remains at its current tracked path;
- fresh DCC sources use a new {ASSET_ID} directory under SourceAssets/Blender;
- fresh exports use a new {ASSET_ID} directory under SourceAssets/Exports;
- fresh textures use a new {ASSET_ID} directory under SourceAssets/Textures;
- transient proof and automation outputs use a new {ASSET_ID} directory under
  Saved/Automation;
- Unreal assets use a new {ASSET_ID} path under Content/Aerathea only after the
  Unreal step is authorized.

No fresh output directory may share a path with A001-A004.

## 8. Standard Step Contract

Before any step begins, the active agent must present:

- step ID and name;
- one decision the step must produce;
- governing Core principle;
- exact authorizing plan section;
- approved inputs;
- allowed files;
- blocked files;
- allowed actions;
- blocked actions;
- expected outputs;
- validators;
- visible review requirement, if any;
- artifact status on pass;
- artifact status on failure;
- stop conditions;
- smallest sufficient change;
- estimated context demand;
- planned checkpoint points.

The step begins only after Flamestrike approves that exact contract or an
already approved handoff explicitly authorizes it under Core.

## 9. Standard Step Completion Gate

A step is complete only when:

- every required output exists at the declared path;
- every input and output hash is recorded;
- focused validators pass;
- the evidence answers the step's one decision;
- no blocked file was modified;
- no adjacent step was started;
- assumptions and interpretations are listed;
- all artifacts are classified;
- failed or rejected outputs are preserved and labeled;
- the local step output record is complete;
- the artifact index and approval log are current;
- RESET_RESUME_STATE identifies the last Core-valid state;
- a next-agent handoff exists;
- pre/post checkpoints are recorded when required;
- scoped tracked work is committed and pushed after approval and according to
  Core;
- Flamestrike is told whether the step passed, failed, or is blocked;
- Flamestrike is told to restart with a new agent.

If any item is missing, the step remains in progress or blocked. It must not be
reported as complete.

## 10. Context And Restart Protocol

### Mandatory Session Boundary

One agent session owns one complete production step.

After every completed step:

1. save and validate;
2. create the handoff package;
3. checkpoint;
4. commit and push the approved scoped tracked work;
5. report the exact next step;
6. tell Flamestrike to restart with a new agent;
7. stop.

The same agent must not begin the next production step.

### Context Budget

Proposed controls:

- 200k tokens: warning threshold; stop expanding scope and assess whether the
  current step can finish with full validation and handoff;
- 220k tokens: handoff reserve threshold; do not begin another build, render,
  import, or broad audit;
- 240k tokens: mandatory stop ceiling; preserve the last safe state and create
  an incomplete-step handoff if the step is not complete.

The 20k reserve between 220k and 240k exists for validation, status correction,
checkpointing, and handoff. It must not be spent on new production.

When exact context usage is not visible, enforce one step per session and split
any step whose expected work includes more than one major build/validation
loop.

Context pressure is not permission to:

- skip validation;
- declare an incomplete step complete;
- omit artifact classifications;
- continue into the next step;
- perform a rushed repair-forward pass.

### Incomplete-Step Handoff

If a step cannot finish safely before the context ceiling:

- stop at the last non-destructive boundary;
- do not claim pass;
- mark the step in progress or blocked;
- list completed and uncompleted contract items;
- record live processes and partial outputs;
- classify partial outputs as candidate, proof only, quarantined, or invalid;
- checkpoint;
- create a same-step resume handoff;
- tell Flamestrike to restart with a new agent to continue the same step.

## 11. Next-Agent Read Order

On restart, the next agent reads only:

1. AGENTS.md;
2. this approved plan;
3. {ASSET_ID}_RESET_RESUME_STATE.md;
4. the immediately previous step output record;
5. the current step contract;
6. manifests explicitly named by the current step contract;
7. the source image and scanline manifest when the current step requires them.

The next agent must not begin by reading the complete Cairn Stone history,
legacy A001-A004 outputs, or unrelated project files.

After inspection, the next agent reports:

- where the project stopped;
- current artifact vocabulary;
- last Core-valid state;
- current exact-data authority;
- current interpretation authority;
- proof outputs and manifests;
- what is blocked;
- the exact current step contract.

If the state and handoff disagree, stop.

## 12. Required Handoff Package

Every step produces:

- STEP_XX_CONTRACT.md
- STEP_XX_OUTPUT_RECORD.md
- STEP_XX_VALIDATION_MANIFEST.json
- STEP_XX_TO_STEP_YY_HANDOFF.md
- updated RESET_RESUME_STATE.md
- updated ARTIFACT_INDEX.md
- updated APPROVAL_LOG.md
- relevant hashes and focused validator results
- checkpoint path
- scoped commit hash and push status after approval

Every handoff must state:

- completed step and decision;
- approved goal;
- authority files;
- allowed and blocked data;
- files changed or created;
- evidence produced;
- formulas used;
- assumptions or interpretations;
- validators and exact results;
- artifact statuses;
- last Core-valid state;
- blockers;
- current git state;
- current checkpoint;
- next step ID;
- next step decision;
- next step allowed and blocked scope;
- exact read order;
- next approval gate.

## 13. Multi-Step Process

### Step 01 - Fresh Project Charter And Asset Identity Lock

Decision:

Approve the new asset identity, fresh namespace, project goal, source role,
legacy-data firewall, final completion definition, and record layout.

Allowed:

- create tracked charter, firewall, reset, artifact-index, approval-log, and
  empty step/manifest/handoff directories;
- reference the existing source image without copying or altering it.

Blocked:

- measurement;
- source cropping;
- masks;
- scripts;
- generated imagery;
- geometry;
- DCC or Unreal work;
- reuse or deletion of legacy outputs.

Pass outputs:

- approved project charter;
- approved fresh-start data firewall;
- locked asset ID;
- initialized RESET_RESUME_STATE;
- initialized artifact and approval indexes.

Approval gate:

Flamestrike approves the exact identity and fresh-start boundary.

Restart:

Mandatory after completion.

### Step 02 - Source Authority And Scanline Lock

Decision:

Prove that the confirmed source and its scanline record are intact, exact, and
the sole asset-specific source authority.

Allowed:

- non-mutating file/hash inspection;
- fresh exact scanline verification if required;
- creation of source-lock and verification records.

Blocked:

- image cleanup;
- color correction;
- resizing;
- resampling;
- panel extraction;
- geometry or interpretation.

Pass conditions:

- source file hash recorded;
- source pixel hash recorded;
- width and height recorded;
- max_rgb_delta = 0;
- changed_pixels = 0;
- pixel_exact = true;
- target and rebuild hashes match.

Pass status:

Source image and scanline evidence become authoritative for the fresh project.

Restart:

Mandatory after completion.

### Step 03 - Exact Panel Decomposition

Decision:

Lock lossless full-source crop formulas for perspective, front, back, left,
right, and top panels while excluding borders and unrelated annotations from
panel ownership.

Allowed:

- integer, half-open crop coordinates;
- lossless extraction with no scaling or filtering;
- source-only crop-boundary overlays;
- pixel hash comparison between each crop and its source region.

Blocked:

- component masks;
- candidate fills;
- silhouette cleanup;
- annotation removal from the actual crop;
- geometry;
- texture synthesis.

Pass outputs:

- panel crop manifest;
- lossless panel images;
- crop-boundary evidence board showing only source pixels and exact boundaries;
- per-panel hashes;
- perspective panel classified as visual corroboration unless separately
  calibrated.

Approval gate:

Flamestrike approves the panel boundaries as source ownership.

Restart:

Mandatory after completion.

### Step 04 - Physical Component And Source-Ownership Inventory

Decision:

Identify every visibly separate physical component or layer, assign fresh
neutral component IDs, and record ambiguous or occluded boundaries without
solving them.

Allowed:

- source-pixel point and boundary marks;
- exact visible contact lines;
- component ownership tables;
- blocked-unknown labels;
- source-only evidence boards.

Blocked:

- preloading old component names or counts;
- inferred component fills;
- hidden geometry;
- smoothing;
- mesh planning;
- using color threshold alone as geometry authority.

Pass outputs:

- fresh component inventory;
- source-view ownership matrix;
- visible/occluded/ambiguous classification;
- initial contact-line inventory;
- list of blocked unknowns.

Approval gate:

Flamestrike approves the component decomposition or marks it blocked.

Restart:

Mandatory after completion.

### Step 05 - Pixel Convention, Coordinate Frame, And Registration Lock

Decision:

Lock the measurement convention, world axes, origin policy, center authority
types, orientation pixels, view correspondence IDs, and registration rules.

Allowed:

- formula and coordinate records;
- exact source-pixel marks;
- review-only overlays that cannot enter textures or geometry.

Blocked:

- moving, rotating, scaling, or centering a component;
- selecting a bounding-box center for an irregular component;
- deriving geometry.

Pass outputs:

- pixel convention record;
- coordinate-frame record;
- orientation-pixel manifest;
- seam/corner/contact correspondence IDs;
- registration evidence board;
- declared tolerances for later audits.

Approval gate:

Flamestrike approves the convention and registration authority.

Restart:

Mandatory after completion.

### Step 06 - Front And Back Exact Measurement Contracts

Decision:

Derive formula-linked calibration, visible contours, centers, height stations,
component boundaries, contact lines, and source-owned feature measurements from
the front and back panels.

Allowed:

- exact source pixels;
- approved panel crops;
- approved component IDs;
- approved convention and registration marks;
- source-only measurement marks and pass/fail evidence.

Blocked:

- candidate fills;
- inferred backsides;
- average front/back dimensions;
- geometry previews;
- old crop or formula constants.

Pass outputs:

- front measurement manifest;
- back measurement manifest;
- front/back calibration records;
- front/back measurement contracts;
- front/back disagreement list;
- source-only measurement review artifact.

Pass rule:

Every measurement links to source pixels and a declared formula. Unresolved
disagreement remains blocked, not averaged.

Restart:

Mandatory after completion.

### Step 07 - Left And Right Exact Measurement Contracts

Decision:

Derive formula-linked calibration, visible side contours, centers, thickness
stations, component boundaries, contact lines, and source-owned feature
measurements from the left and right panels.

Allowed and blocked scope:

The same controls as Step 06, applied only to left and right panels.

Pass outputs:

- left measurement manifest;
- right measurement manifest;
- left/right calibration records;
- left/right measurement contracts;
- left/right disagreement list;
- source-only measurement review artifact.

Pass rule:

No left/right averaging and no visual thickness fitting.

Restart:

Mandatory after completion.

### Step 08 - Top Exact Measurement Contracts

Decision:

Derive formula-linked calibration, visible footprints, outer and inner
perimeters, pixel-count center types, component ownership, orientation, and
contact relationships from the top panel.

Allowed:

- source-owned contours;
- filled-footprint calculations only when their formula and annotation
  exclusion are approved;
- separate outer contour, inner contact perimeter, visible annulus, and shared
  stacked-layer envelope records.

Blocked:

- rectangular footprint substitution;
- ellipse or superellipse substitution;
- shared contour duplicated as proof for multiple hidden layers;
- invented bottom footprint;
- candidate geometry.

Pass outputs:

- top calibration record;
- top measurement manifest;
- perimeter and center manifests;
- visible/occluded/inferred sector classification;
- top-view disagreement list;
- source-only measurement review artifact.

Restart:

Mandatory after completion.

### Step 09 - Cross-View Correspondence And Exact Dataset Audit

Decision:

Determine whether the exact front, back, left, right, and top datasets can be
registered into one coherent measurement authority without averaging,
stretching, silent selection, or interpretation.

Allowed:

- correspondence tables;
- exact formula comparison;
- tolerance audit;
- disagreement matrix;
- pass/fail/blocked classification.

Blocked:

- geometry;
- smoothing;
- view prioritization not already approved;
- choosing a convenient measurement;
- repairing a disagreement.

Pass outputs:

- integrated exact measurement index;
- cross-view correspondence manifest;
- disagreement and unknown matrix;
- pre-geometry exact-data audit.

Pass rule:

The exact dataset may pass with explicitly blocked unknowns. It may not pass by
hiding disagreement.

Restart:

Mandatory after completion.

### Step 10 - Unknowns And Interpretation Decision Gate

Decision:

Flamestrike approves, rejects, or leaves blocked every unavoidable geometry
unknown required for a coherent 360-degree object.

Expected unknown classes:

- bottom surface;
- fully occluded interfaces;
- hidden contact fill;
- source-invisible topology;
- cross-view disagreement selections;
- sectors not owned by a visible source view.

Allowed:

- written interpretation options;
- source-only evidence beside clearly separated interpretation diagrams;
- explicit rule proposals;
- approval, rejection, or blocked decisions.

Blocked:

- implementation;
- geometry creation;
- presenting an interpretation as measurement;
- silently choosing a rule.

Pass outputs:

- approved geometry-interpretation manifest;
- rejected-option record;
- remaining blocked-unknown list;
- explicit source-versus-interpretation ownership map.

Pass rule:

No required unknown may enter geometry without an approved rule.

Restart:

Mandatory after completion.

### Step 11 - Production Specification And Geometry Construction Blueprint

Decision:

Approve a buildable construction blueprint that maps every planned visible
vertex, contour, component, interface, and hidden fill to exact evidence or an
approved interpretation rule.

Required content:

- asset name and Static Mesh role;
- scale and coordinate frame;
- component construction order;
- per-feature measurement contract links;
- topology ownership;
- pivot plan;
- modular-versus-combined runtime plan;
- UV and material slot strategy at planning level;
- triangle target;
- LOD strategy;
- collision strategy;
- export paths;
- Unreal paths;
- validators;
- review views and camera alignment;
- blocked methods.

Blocked:

- DCC creation;
- scripts that generate geometry;
- texture production;
- Unreal work.

Approval gate:

Flamestrike approves the construction blueprint before geometry.

Restart:

Mandatory after completion.

### Step 12 - DCC Source Geometry Candidate

Decision:

Build one fresh DCC source candidate that satisfies the approved exact
measurement contracts and geometry-interpretation manifest.

Allowed:

- fresh generator or controlled Blender construction;
- component-separated geometry;
- exact scale and pivot setup;
- measurement-driven topology;
- proof-only DCC renders after numeric audit passes.

Blocked:

- old builder reuse;
- projection shells as final geometry;
- detached carriers;
- source-sheet planes in the asset;
- geometry from diagnostic masks;
- unapproved smoothing or fitting;
- UV, final texture, LOD, collision, FBX, or Unreal escalation.

Pass outputs:

- Blender DCC source candidate;
- generator and audit scripts;
- geometry manifest;
- numeric audit;
- source-aligned proof renders;
- review board only after audit pass.

Pass status:

DCC source candidate, not DCC game-ready.

Restart:

Mandatory after completion.

### Step 13 - DCC Geometry Audit And Flamestrike Review

Decision:

Approve, reject, or block the DCC source candidate against the source image,
exact measurement contracts, approved interpretations, 360-degree coherence,
and Aerathea visual requirements.

Allowed:

- non-mutating DCC audit;
- exact source overlays;
- fixed-camera source comparisons;
- visible review window;
- defect and mismatch records.

Blocked:

- geometry repair during the review step;
- UV or texture work;
- LOD, collision, export, or Unreal work.

Pass outputs:

- geometry audit record;
- visual review decision;
- approved candidate hash or rejected/blocked artifact classification;
- next-step authority only on approval.

Restart:

Mandatory after completion, including after rejection or block.

### Step 14 - UV, Base Color, And Material-Interpretation Plan

Decision:

Approve how source-owned visible RGB pixels, hidden Base Color areas, UV seams,
Normal, ORM, AO, roughness, metallic, and any emissive behavior will be handled
without mislabeling authored maps as exact image data.

Exact authority:

- visible source-owned Base Color pixels;
- approved color ownership regions;
- exact source RGB and pixel hashes.

Interpretation requiring approval:

- hidden-surface Base Color continuation;
- UV seam placement;
- normal-map detail;
- roughness;
- metallic values;
- ambient occlusion;
- bake settings;
- mip and filtering behavior;
- any emissive behavior.

Blocked by default:

- emissive red markings;
- filtered resampling of visible canon pixels;
- color grading;
- material response inferred from appearance without an approved rule.

Pass outputs:

- UV ownership plan;
- Base Color ownership manifest;
- material-interpretation manifest;
- texture naming, resolution, packing, filtering, and validation plan.

Restart:

Mandatory after completion.

### Step 15 - UV And Texture/Material Candidate

Decision:

Create and validate the approved UVs, Base Color, Normal, ORM, and material
candidate without changing approved geometry.

Allowed:

- UV unwrap under the approved plan;
- exact visible Base Color transfer;
- approved hidden-area treatment;
- approved Normal and ORM authoring;
- material preview after pixel and map audits pass.

Blocked:

- geometry changes;
- unapproved color correction;
- texture synthesis outside approved rules;
- LOD, collision, FBX, or Unreal escalation.

Pass outputs:

- UV-ready Blender candidate;
- texture maps;
- material candidate;
- visible-pixel exactness audit;
- UV audit;
- fixed-camera material proof renders.

Pass status:

Candidate pending focused review; not DCC game-ready.

Restart:

Mandatory after completion.

### Step 16 - DCC Game-Ready Package

Decision:

Create the optimized DCC package with LOD0-LOD3, collision proxy, final pivot,
approved material slots, scale, and valid FBX exports.

Allowed:

- optimization that preserves approved silhouette and measurement tolerances;
- LOD construction;
- collision proxy;
- FBX export;
- focused imported-FBX validation;
- final DCC proof renders after technical pass.

Blocked:

- source-visual redesign;
- material redesign;
- silent topology changes that alter approved visible measurements;
- Unreal import.

Pass outputs:

- Blender source;
- LOD0-LOD3;
- collision proxy;
- FBX package;
- texture package;
- export manifest;
- imported-FBX triangle and geometry proof;
- DCC game-ready review board.

Pass status:

DCC game-ready candidate, not fully game-ready.

Restart:

Mandatory after completion.

### Step 17 - DCC Game-Ready Audit And Flamestrike Review

Decision:

Approve, reject, or block the complete DCC game-ready candidate before Unreal.

Required validation:

- source and measurement fidelity;
- approved 360-degree geometry;
- UV and visible-pixel exactness;
- material read;
- LOD silhouette preservation;
- collision suitability;
- pivot and scale;
- FBX content validity;
- triangle, texture, and material budgets.

Blocked:

- repair during review;
- Unreal import before approval.

Pass outputs:

- final DCC audit;
- visible review decision;
- approved DCC package hash set;
- Unreal handoff manifest.

Restart:

Mandatory after completion.

### Step 18 - Unreal Import Candidate

Decision:

Import and configure the approved DCC package in Unreal without changing its
approved visual identity.

Allowed:

- Static Mesh import;
- LOD assignment;
- collision assignment;
- texture import;
- material and material-instance setup;
- metadata;
- approved review-map placement;
- focused validators.

Blocked:

- asset redesign;
- source or DCC edits;
- unrelated map changes;
- final visual approval claim.

Pass outputs:

- Unreal import candidate;
- import/configuration manifest;
- focused technical validator results;
- review placement;
- clean offscreen capture preparation.

Restart:

Mandatory after completion.

### Step 19 - Unreal Technical Validation And Visual Review

Decision:

Approve, reject, or block the Unreal import candidate after technical validation
and a source/DCC/Unreal orientation-matched visual comparison.

Required checks:

- correct asset loaded;
- correct scale;
- correct pivot;
- material slots and textures;
- LODs;
- collision;
- bounds;
- orientation;
- lighting and material read;
- camera alignment;
- no proxy, underside, clipping, or mismatched asset;
- source, DCC, and Unreal A/B comparison.

Allowed:

- non-mutating validation;
- offscreen capture;
- marker pass when orientation is uncertain;
- visible review window.

Blocked:

- repair during review;
- gameplay or performance completion claim before the next step.

Pass status:

Validated Unreal import candidate pending gameplay/performance validation.

Restart:

Mandatory after completion.

### Step 20 - Gameplay/Review-Map And Performance Validation

Decision:

Prove that the asset functions at intended scale and performance in an approved
Unreal gameplay or review context.

Required checks:

- scale against intended environment or character anchor;
- collision behavior;
- LOD transitions;
- material and texture behavior at runtime;
- draw calls;
- triangle counts;
- material count;
- texture sizes;
- shader cost;
- lighting readability;
- stability and startup validation when relevant.

Blocked:

- asset redesign;
- unrelated environment work;
- final library classification before Flamestrike approval.

Pass outputs:

- gameplay/review-map validation report;
- performance report;
- clean final review captures;
- final approval package.

Restart:

Mandatory after completion.

### Step 21 - Final Flamestrike Approval And Library Closeout

Decision:

Approve, reject, or block the asset for the Aerathea asset library.

Required review:

- confirmed source;
- approved exact measurement authority;
- approved interpretation records;
- DCC proof;
- Unreal proof;
- gameplay/performance proof;
- final artifact index;
- unresolved limitations.

On approval:

- classify the asset as Approved library asset;
- update visual canon and asset indexes only as explicitly authorized;
- record final paths, hashes, validators, and approval;
- create final closeout and reusable pipeline lessons;
- checkpoint, commit, and push scoped tracked work;
- create a final restart-safe archive/handoff record.

On rejection or block:

- preserve current outputs;
- record the exact failed gate;
- do not repair forward;
- return to the last approved step or present a Core recovery plan.

Restart:

Mandatory after closeout so future work begins from the final authoritative
state rather than the production session context.

## 14. Efficiency Controls

Efficiency means reducing rework without weakening evidence.

Required:

- one decision per step;
- deterministic structured manifests from the first source step;
- validate before rendering;
- render only after technical pass;
- open only approval-ready visual artifacts;
- use one fresh project namespace;
- preserve stable hashes between gates;
- fail early on missing formulas, mismatched hashes, unauthorized paths, and
  source disagreement;
- keep measurement boards source-only;
- keep interpretation boards visibly separate;
- do not create tooling unless the current step needs it;
- do not run Blender or Unreal during planning or measurement-only steps;
- do not parallelize this asset across agents unless Flamestrike explicitly
  approves disjoint lanes after the exact-data authority is locked;
- split an oversized step before execution rather than crossing the 240k
  context ceiling.

## 15. Standard Restart Notification

At the end of every completed step, report:

Step XX is complete.

- Decision: pass, rejected, or blocked.
- Last Core-valid state: [exact record].
- Authoritative outputs: [paths and statuses].
- Checkpoint: [path].
- Commit/push: [hash and status].
- Next step: Step YY [name].
- Next approval needed: [exact gate].

Restart now with a new agent. The next agent must read AGENTS.md, the approved
fresh-start plan, RESET_RESUME_STATE, the Step XX output record, and the Step YY
contract. The current agent must not begin Step YY.

## 16. Approved Plan-Level Decisions

1. A completely new asset revision ID and namespace must not reuse A001-A004
   paths. The exact ID will be selected and approved in Step 01.
2. A001-A004 asset-specific data is prohibited as production input. Generic
   Core/AetherForge lessons remain allowed.
3. Unavoidable hidden and material data may enter only through explicit
   interpretation gates approved by Flamestrike.
4. Context controls are 200k warning, 220k handoff reserve, and 240k mandatory
   stop.
5. One complete production step is allowed per agent session, followed by a
   mandatory restart.
6. Plan approval authorizes process structure only. Step 01 requires a separate
   visible contract.
7. The final goal is Approved library asset status, including Unreal,
   gameplay/review-map, performance, and final aesthetic validation.

## 17. Plan Approval Record

Decision: approved.

Approver: Flamestrike.

Approval date: 2026-07-15.

Approval statement: "I approve the Plan."

Approved artifact status: authoritative process plan.

Next gate: Step 01 - Fresh Project Charter And Asset Identity Lock.

Step 01 is not authorized by this approval. It requires a new visible step
contract after restart.
