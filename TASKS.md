# Tasks: The Work That Is Yours

The scaffold gives you a finished Revision A one-line diagram, the
paperwork system, and the reference sheets. The four tasks below are
the project. Each one has a checklist and a plain statement of what
done looks like.

Work in LibreCAD (free, opens and saves DXF directly) or an AutoCAD
trial. What matters is the drawing practice, not the tool brand.

## Task 1: Draw the lineup elevation, D-202

A one-line diagram shows how the gear connects. An elevation shows
what it physically looks like from the front: the sections standing
side by side, the doors, the breaker positions, the dimensions a
customer or an installer works from.

- [ ] Create drawing D-202, the front elevation of the same lineup
      as D-201: a main section and two feeder sections
- [ ] Show each section as a rectangle with its door outline, and
      the breaker in each section drawn in its compartment
- [ ] Mark the transformer T1 as an external unit beside the lineup,
      since it is not inside a switchgear section
- [ ] Dimension the drawing: overall width, overall height, and
      section widths, using dimension lines, not loose text
- [ ] Fill in a title block: drawing number D-202, Revision A, your
      name as drawn by, "SHEET: 2 OF 2"
- [ ] Export a PNG or PDF preview and save it next to the drawing

**Done looks like:** drawings/D-202_lineup-elevation_revA.dxf (or
.dwg) exists with a preview beside it. A stranger can count the
sections, tell which breaker lives in which section, and read the
lineup's overall size off the dimensions.

## Task 2: Work the redline into D-201 Revision B

Open drawings/MARKUP.md. It lists four changes against Revision A:
a renamed load, a changed breaker rating, a new PT branch, and
title block corrections.

- [ ] Copy the Rev A file to a new Rev B file (never edit the
      released Rev A file itself)
- [ ] Make all four markup changes
- [ ] Set the title block to REV: B, SHEET: 1 OF 2, your name,
      today's date
- [ ] Export a fresh preview of Revision B

**Done looks like:** drawings/D-201_one-line_revB.dxf exists, every
markup item is visible in it, and Revision A on disk is untouched.

## Task 3: Run the change through the paperwork

A revision without paperwork is just a file someone edited. Run
Revision B through the same system the worked example used.

- [ ] Fill in a copy of paperwork/ECO_template.md as ECO-0002,
      covering the redline changes (all four items are one change:
      the markup package)
- [ ] Add the Revision B row for D-201 and the Revision A row for
      D-202 to paperwork/revision_log.md
- [ ] Run paperwork/drawing_package_checklist.md against the
      two-sheet package and tick what is true. Anything you cannot
      tick, write down why in the ECO disposition

**Done looks like:** ECO-0002 is complete enough that a stranger
could reconstruct what changed, why, and under whose approval. The
revision log agrees with both title blocks.

## Task 4: Windchill and SAP, in your own words

- [ ] Write the half page in reference/windchill_and_sap.md,
      answering the guiding questions there

**Done looks like:** two short sections, one per system, that say
what each system holds in the life of an order and where the handoff
between them happens. No vendor language.
