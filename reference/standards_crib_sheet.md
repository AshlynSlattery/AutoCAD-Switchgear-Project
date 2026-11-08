# Standards Crib Sheet: Switchgear Work

One page of the standards that govern drawings like D-201. You do not
need to own these or read them cover to cover. You need to know each
one exists, what it covers, and when a project engineer would reach
for it.

## How the gear is built and rated

- **IEEE C37.20.2, Metal-Clad Switchgear.** The construction and
  rating standard for metal-clad switchgear, the kind with drawout
  vacuum breakers in separate compartments. Most medium-voltage
  lineups in North America are built to this.
- **IEEE C37.20.3, Metal-Enclosed Interrupter Switchgear.** The
  equivalent standard for switchgear built around load interrupter
  switches and fuses instead of power circuit breakers.
- **IEEE C37.20.1, Metal-Enclosed Low-Voltage Power Circuit Breaker
  Switchgear.** The low-voltage counterpart to C37.20.2, for gear at
  1000 V and below.
- **UL 1558, Metal-Enclosed Low-Voltage Power Circuit Breaker
  Switchgear.** The UL product safety standard that low-voltage
  switchgear is listed to. Where IEEE standards say how gear is
  rated and tested, UL listing is what an inspector looks for.

## The breakers themselves

- **IEEE C37.04, Rating Structure for AC High-Voltage Circuit
  Breakers.** Defines what the ratings on a breaker nameplate mean:
  rated voltage, short-circuit current, interrupting time.
- **IEEE C37.06, Preferred Ratings for AC High-Voltage Circuit
  Breakers.** The table of standard rating combinations breakers are
  actually bought in. When a spec says a breaker "is not a preferred
  rating", this is the table it means.
- **IEEE C37.09, Test Procedure for AC High-Voltage Circuit
  Breakers.** How the type tests behind those ratings are run.
- **IEEE C37.010, Application Guide for AC High-Voltage Circuit
  Breakers.** How to pick a breaker for a real system: duty cycle,
  transient recovery voltage, out-of-phase switching, and the rest
  of what a nameplate does not tell you.

## The numbers on the drawing

- **IEEE C37.2, Electrical Power System Device Function Numbers.**
  The numbering system for protective and control devices. It is why
  every breaker on the one-line is a "52" (52 is the AC circuit
  breaker function), and why relays are 50/51 (instantaneous and
  time overcurrent), 27 (undervoltage), 59 (overvoltage), and 87
  (differential). When a schematic shows a device number, this
  standard is the dictionary.

## How the gear gets installed (NEC, NFPA 70)

- **Article 408, Switchboards, Switchgear, and Panelboards.**
  Installation rules for the gear itself, including clearances and
  marking.
- **Article 490, Equipment for General Use, Over 1000 Volts.** The
  medium-voltage installation rules: wiring methods, guarding, and
  clearances for equipment like the D-201 lineup.
- **Article 450, Transformers and Transformer Vaults.** The rules
  covering transformer T1: protection, ventilation, and when a vault
  is required.
- **Article 240, Overcurrent Protection.** Where breakers and fuses
  must be placed and how they are sized to protect conductors.
- **Article 250, Grounding and Bonding.** The grounding rules every
  lineup is installed under.
- **Section 110.16, Arc-Flash Hazard Warning.** Requires the
  arc-flash warning labels that go on the front of the gear.

## Safety performance

- **IEEE C37.20.7, Guide for Testing Switchgear for Internal Arcing
  Faults.** Defines arc-resistant ratings and how they are tested.
  "Arc-resistant, Type 2B" on a submittal traces back to this guide.
- **IEEE 1584, Guide for Performing Arc-Flash Hazard Calculations.**
  The method behind the incident-energy numbers on arc-flash labels
  and the study that produces them.
