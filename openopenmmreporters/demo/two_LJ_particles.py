from simtk import openmm as mm
from simtk.openmm import app
import simtk.unit as unit
import numpy as np

def two_LJ_particles(platform_name='CUDA'):

    # Parameters

    mass = 100.0 * unit.amu
    sigma = 2**(11.0/6.0) * unit.angstroms       # radius = 2.0  angstroms
    epsilon = 1.0 * unit.kilocalories_per_mole
    charge = 0.0 * unit.elementary_charge

    box = np.array([[3.0, 0.0, 0.0], [0.0, 3.0, 0.0], [0.0, 0.0, 3.0]])*unit.nanometers
    coordinates = np.array([[0.0, 0.0, 0.0], [0.0, 1.5, 0.0]])*unit.nanometers
    velocities = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])*unit.nanometers/unit.picoseconds

    temperature = 300.0*unit.kelvin
    collisions_rate = 1.0/unit.picoseconds
    integration_timestep = 2.0*unit.femtoseconds

    cutoff_distance = 1.2*unit.nanometers
    switching_distance = 0.9*unit.nanometers

    # Topology

    topology = app.Topology()

    try:
        dummy_element = app.element.get_by_symbol('DUM')
    except:
        dummy_element = app.Element(0, 'DUM', 'DUM', mass)

    dummy_element.mass._value = mass.value_in_unit(unit.amu)

    chain = topology.addChain('A')

    for ii in range(2):
        residue = topology.addResidue('DUM', chain)
        atom = topology.addAtom(name='DUM', element= dummy_element, residue=residue)

    topology.setPeriodicBoxVectors(box)

    # System

    system = mm.System()

    non_bonded_force = mm.NonbondedForce()
    non_bonded_force.setNonbondedMethod(mm.NonbondedForce.CutoffPeriodic)
    non_bonded_force.setUseSwitchingFunction(True)
    non_bonded_force.setCutoffDistance(cutoff_distance)
    non_bonded_force.setSwitchingDistance(switching_distance)

    system.addParticle(dummy_element.mass)
    non_bonded_force.addParticle(charge, sigma, epsilon)

    system.addParticle(dummy_element.mass)
    non_bonded_force.addParticle(charge, sigma, epsilon)

    _ = system.addForce(non_bonded_force)

    system.setDefaultPeriodicBoxVectors(box[0], box[1], box[2])

    # Simulation

    integrator = mm.LangevinIntegrator(temperature, collisions_rate, integration_timestep)
    platform = mm.Platform.getPlatformByName(platform_name)

    simulation = app.Simulation(topology, system, integrator, platform)

    simulation.context.setPositions(coordinates)
    simulation.context.setVelocities(velocities)

    return simulation

