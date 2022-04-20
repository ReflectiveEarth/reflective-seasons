# reflective-seasons

### An empirical analysis of Earth's seasonal surface reflectivity potential

Reflective Earth is on a mission to slow global warming as fast and safely as
possible by increasing Earth's reflectivity to reduce its energy imbalance.
Reflectivity interventions reduce the amount of sunlight absorbed by the Earth
system, i.e. the amount of energy entering the system. Deploying reflective
materials as a stop gap could limit the amount of warming experienced by people
and buy society time to reduce greenhouse gas emissions and drawdown atmospheric
greenhouse gas concentrations.

The potential of reflective materials to reflect sunlight strongly depends on
location. The amount of incoming solar radiation varies greatly, with more
being received in the tropics and less being received at the poles. Clouds,
water vapor, and aerosols (e.g. dust, smoke) scatter and absorb sunlight. These
properties vary spatially as well.

This code repository contains workflows to explore the seasonality of Earth's
potential surface-reflected outgoing solar radiation (which we refer to as
*outsolation*). We use data from the National Aeronautics and Space
Administration (NASA) Clouds and the Earth's Radiant Energy System (CERES)
Energy Balanced and Filled (EBAF) satellite-derived product, specifically
radiative fluxes at the surface and top of atmosphere. This allows us to
estimate surface reflectance and atmospheric transmittance and reflectance.
When averaged over several decades, these properties can be combined with
incoming solar radiation and surface albedo to model the potential
surface-reflected outgoing solar radiation. See our earlier analysis
[`reflective-potential`][reflective-potential] for more details on the
underlying methods.

## Support

Read the [support][support] guidelines for guidance on how to reach out for help
with this project.

## Contributing

We welcome contributions that improve the quality of our code and/or science.
Before you dive in, read the [contribution][contributing] guidelines.

## Code of Conduct

This project has a [code of conduct][conduct]. By interacting with this
repository, organization, or community you agree to abide by its terms.

## License

[Clear BSD][license] © 2022 [Reflective Earth][author]

<!-- Definitions -->

[author]: https://www.reflectiveearth.org
[conduct]: CODE_OF_CONDUCT.md
[contributing]: CONTRIBUTING.md
[license]: LICENSE.md
[support]: SUPPORT.md
[reflective-potential]: https://github.com/ReflectiveEarth/reflective-potential
