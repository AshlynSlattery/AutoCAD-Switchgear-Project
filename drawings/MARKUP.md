# Redline Markup for D-201, Revision A to Revision B

These are review comments written against Revision A of the one-line
diagram (drawings/D-201_one-line_revA.dxf). Working through them and
issuing the drawing as Revision B is one of your tasks in TASKS.md.
Each item says what changes and where.

1. **Feeder 2 load name.** The load on FDR-02 is labeled "MOTOR LOAD".
   The mechanical contractor confirmed this feeder serves the chiller
   plant. Rename the load to "CHILLER PLANT".

2. **Feeder 1 breaker rating.** The FDR-01 breaker callout reads
   "1200 A FRAME". The feeder cable and the load study both came back
   at 2000 A. Change the callout to "2000 A FRAME".

3. **Add a potential transformer (PT) branch on the main bus.** The
   relaying package needs a bus voltage source. Add a branch off the
   main bus between the main breaker and FDR-01: a fused disconnect
   (three fuse symbols or one fuse symbol with a "3X" note), a PT
   symbol (two overlapping circles, smaller than the power
   transformer), and the label "PT, 12470 V TO 120 V, FOR RELAYING AND
   METERING".

4. **Title block corrections.** The package now has a second sheet
   (your lineup elevation, D-202), so "SHEET: 1 OF 1" becomes
   "SHEET: 1 OF 2". Set "REV: A" to "REV: B" and update the date to
   the day you issue it. Fill in the "DRAWN BY" field with your name.

When you issue Revision B, save it as a new file
(drawings/D-201_one-line_revB.dxf). Never overwrite Revision A. A
released revision is a record, and the next reviewer needs to see
exactly what changed.
