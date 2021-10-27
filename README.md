# Foxes-Rabbits
This repository will contain all 3 phases of the programming for our final assestment

PHASE 1:
This project will focus on simulations and make the following simplifying assumptions about the
model:
1. The food supply for the prey population is replenished at a constant rate.
2. The food supply for the predator population depends on the prey population.
3. Reproduction is asexual: a mature individual reproduces with a fixed probability provided that it is well-fed and there are no predators nearby.
4. The environment does not change over time in favour of either population making evolution
inconsequential.

Foxes and Rabbits
The environment in this simulation is a finite 2D grid (a rectangle or a toroid) with a fixed size. The
coordinate system is oriented north-to-south and west-to-east. On this grid we find foxes (predators),
rabbits (preys) and grass. On each cell there can be at most one fox and at most one rabbit (a fox
and rabbit can be on the same spot at the same time but not two rabbits or two foxes). There is a
fixed limit on the amount of grass on each cell. This grid evolves over time in discrete steps: at each tick of the simulation clock animals move,
feed, reproduce, and grass grows.

Animals can move along the north-south and west-east directions one cell at a time, provided
that the destination cell is not occupied by an animal of the same species. Below are all the possible
evolutions of a 3x3 grid where the animal in central cell takes a step. On the left all four directions
are free whereas on the right the north and west directions are blocked by the presence of an animal
of the same species.

The choice of destination is random following a uniform probability distribution.
Animals can reproduce at any time provided that:
1. they reached maturity (they have at least a certain age),
2. they are well-fed (they have eaten enough food),
3. they are safe from predation (a fox is always safe, a rabbit is safe if there are no foxes in its cell
and the ones adjacent to it),
4. one of the adjacent cells can host the newborn.
The cell for the newborn is selected randomly.

Both foxes and rabbits have a level of energy that is replenished eating food. A fixed amount of
energy consumed at each tick of the simulation clock (animal metabolism) and during reproduction.
If an animal runs out of energy it dies of starvation. The maximum amount of energy an animal can
have is fixed.
All animals have an age and the maximum age for a foxes and for rabbits is fixed. When an animal
reaches the maximum age for its species it dies of old age.

PHASE 2:

