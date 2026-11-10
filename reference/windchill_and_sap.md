# Windchill and SAP: What Each One Holds

Your half-page write-up goes in this file (see Task 4 in TASKS.md).
Half a page of your own words. The questions below are the shape of
it. Answer them from what you read and from the ABB order process,
not by copying a vendor page.

## Guiding questions

1. An order comes in for a switchgear lineup. Which system holds the
sales order, the delivery date, and the price?
2. The engineer opens the one-line diagram to revise it. Where does
the controlled copy of that drawing live, and what stops two
engineers from editing it at once?
3. The change gets approved. Which system carries the change object
(the ECO) and the approval signatures? Which system feels the
effect, in the form of a changed bill of materials or a changed
purchase order?
4. Production builds the lineup. Which system tells the floor what
to build, in what order, and records what actually got built?
5. Ten years later a customer asks what revision of the drawing
their gear was built to. Which system answers, and how?

## Your write-up

The PLM Connection (Windchill)



In our manual project workflow, updating to Rev B required saving discrete file copies, manually typing an ECO text file, and pushing updates to GitHub—a process vulnerable to versioning errors and overlapping work. A Product Lifecycle Management (PLM) system like Windchill entirely automates and secures this process. Rather than duplicating files, an engineer "checks out" the drawing, which locks the file system-wide so no one else can make conflicting edits. When the work is done, the PLM system natively handles the Engineering Change Order (ECO) by routing it through a digital signature workflow for review. Once all stakeholders approve the ECO electronically, the system automatically bumps the file revision (e.g., from Rev A to Rev B) and publishes the new version, ensuring perfect version control without relying on manual file management.



The ERP Connection (SAP)



While we skipped generating a Bill of Materials (BOM) for our practice package, in a real-world scenario, a complete BOM listing every 2000 A breaker, transformer, and PT fuse would be pushed seamlessly from Windchill into an Enterprise Resource Planning (ERP) system like SAP. Once the BOM hits SAP, it becomes the operational blueprint for the factory and supply chain teams. Procurement specialists use the system to instantly compare the BOM requirements against current warehouse inventory, automatically generating vendor purchase orders for any missing parts. Simultaneously, the manufacturing teams use the SAP data to allocate shop floor resources and schedule the sheet metal assembly, ensuring that all components and labor converge efficiently at the right workstation.

SAP holds the sales order, delivery date, and price. Windchill answers what revision a customer's gear was built to.

