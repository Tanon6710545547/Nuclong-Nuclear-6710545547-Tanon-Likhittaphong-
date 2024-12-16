Name of project : Nuclong Nuclear 
Project description :
-A nuclear fission chain reaction simulation
-Simulating a nuclear fission reaction with neutrons interacting with uranium.
-The game involves neutrons bouncing off each other and uranium atoms when hit by neutrons
splitting into new elements ((Krypton(Blue),Barium(Yellow)),(Xenon(Orange),Strontium(Pink)),(Cesium(Red),Rubidium(Lime)))
How to install and run the project :
step1 git clone 
step2 cd
step3 run program.
step4 follow the on-screen prompts to enter the number of neutrons and uranium atoms to start the simulation.
Usage :
-Input the number of neutrons and uranium atoms
-The simulation will create (input the number of neutrons) neutrons and (input  the number of uranium atoms) uranium atoms.
-Neutrons will move randomly and trigger fission in uranium atoms, creating new neutrons and fission products.
-The score display will update showing the number of fissions
and different radioactive elements (Krypton, Xenon) will be generated.
Project design and implementation :
-UML class diagram: https://lucid.app/lucidchart/33e99078-7ced-45f3-b582-d9322567c759/edit?viewport_loc=539%2C0%2C1316%2C1511%2CHWEp-vi-RSFO&invitationId=inv_c84fe464-871e-4065-a223-bdae469cb081
--☺class Nucleus:
Presents a nucleus of an atom that can undergo nuclear fission.
In the context of a fission chain reaction simulation,
these nuclei are the primary participants that react to the neutrons in the system.
Neutrons interact with Nucleus objects via the collide() method in the Neutron class.
The ChainReaction class manages a collection of Nucleus objects.
--☺class Neutron:
Presents a single neutron, which is responsible for triggering fission events by interacting with Nucleus objects.
Neutrons can have different velocities and energy levels,
which can change as they interact with nuclei.
Neutrons interact with Nucleus objects through the collide() method.
The ChainReaction class maintains a list of Neutron objects
--☺class ChainReaction:
Is the central class that simulates the fission chain reaction process.
It manages the overall flow of the simulation by coordinating the interactions between Neutron and Nucleus objects.
It tracks the energy produced and ensures that the chain reaction either sustains itself or eventually dies out.
The ChainReaction class manages a collection of Nucleus objects. The simulateStep() method handles the interaction of neutrons with the nuclei.
The ChainReaction class also manages a collection of Neutron objects
--☺class Reactor:
Presents the entire nuclear reactor system where the chain reaction takes place. 
It regulates external factors like temperature and pressure that can influence the fission process.
It provides the necessary environment for the ChainReaction to occur.
The Reactor class holds a reference to the ChainReaction object and simulates the entire reactor's operation.
While the Reactor class does not directly interact with Nucleus or Neutron objects,
it provides the necessary conditions that can affect how the ChainReaction and its constituent particles behave.
-modify-
Neutron Counting;the original code might not track white neutrons, so new versions introduced explicit counting of white neutrons (white_neutrons_count), 
ensuring all increments and decrements happen when white neutrons are created or removed.
Improved Fission Logic;added specific logic to ensure that each fission creates exactly 2 white neutrons, 
along with other color ((Krypton(Blue),Barium(Yellow)),(Xenon(Orange),Strontium(Pink)),(Cesium(Red),Rubidium(Lime))).
Display Updates;Updates to ensure the display correctly shows the counts of elements alongside neutrons.
Physics Accuracy;Improvements to the physics logic for bouncing off walls and uranium, ensuring more realistic behavior during collisions.
Pep8;improved indentation and formatting for readability and to meet Python's Pep8 standards.
-Test Program-
First, the program must be run, and it will prompt for the number of neutrons and uranium atoms.
In this simulation, white balls represent neutrons, and dark green balls represent uranium.
When a collision occurs, fission will randomly result in one of three outcomes: ((Krypton(Blue),Barium(Yellow)),(Xenon(Orange),Strontium(Pink)),(Cesium(Red),Rubidium(Lime))) +2 Neutrons
The simulation ends when all uranium is depleted or the chain reaction completes its predefined limit. Once finished, it will display "Chain Reaction Complete!".
You must also verify that the total number of neutrons counted matches the number of balls present in the system,
including the 6 resulting elements mentioned above (this information will be displayed at the top).
-Problem-
There are times when the movement seems abnormal, 
possibly due to elements accidentally overlapping and pushing each other back and forth.
I tried adding text labels on every circle to make it easier to identify the elements, 
but the elements became too small as a result.
So, I decided not to include the labels (I reduced the element size to make the collisions more visible).