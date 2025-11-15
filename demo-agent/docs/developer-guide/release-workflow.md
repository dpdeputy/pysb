# Release Workflow

This document outlines the process for creating a new release of the `demo_agent` package.

## Release Checklist

- [ ] Ensure all changes for the release are merged into the `develop` branch.
- [ ] Verify that all tests are passing in the CI/CD pipeline.
- [ ] Update the `CHANGELOG.md` with the latest changes.
- [ ] Determine the new version number based on semantic versioning.
- [ ] Create a new release branch from `develop`.
- [ ] Create a release tag (e.g., `v0.1.0`) and push it to the repository.
- [ ] The CI/CD pipeline will automatically build and publish the release.

## Versioning Procedures

This project follows [Semantic Versioning](https://semver.org/). The version number is managed using `hatchling` and is updated based on Git tags.

- **MAJOR** version when you make incompatible API changes.
- **MINOR** version when you add functionality in a backward-compatible manner.
- **PATCH** version when you make backward-compatible bug fixes.

To create a new version, create a new Git tag with the version number (e.g., `v0.1.0`) and push it to the repository.

## Troubleshooting

- **Release build fails:** Check the CI/CD pipeline logs for errors. Common issues include dependency conflicts or test failures.
- **Incorrect version number:** Ensure the Git tag is in the correct format (e.g., `vX.Y.Z`). `hatch-vcs` uses the tag to determine the version.
