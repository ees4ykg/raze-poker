# RAZE Poker

**Risk Attitudes in Zero-sum Encounters**

> 🚧 **Work in progress.** This project is ongoing; code, results and documentation will change.

## Overview

RAZE is a quantitative research project for **ST312 Applied Statistics Project** at the London School of Economics. It asks whether the playing styles of regular online poker players reflect different attitudes to risk.

The project looks at three linked questions:

1. **Playing styles:** Do data-driven clusters of standard betting statistics recover the conventional tight/loose × passive/aggressive typology?
2. **Risk attitudes:** Do style groups differ in how they respond to big wins and losses, and in the edge they demand before calling an all-in?
3. **Theory vs prediction:** Does a decision-theory model predict all-in decisions as well as a machine-learning model given the same information?

## Data

The analysis uses the HandHQ hand histories from Juho Kim's open *A Dataset of Poker Hand Histories* (CC BY 4.0), focusing on PokerStars six-max No-Limit Hold'em from July 2009.

**The data are not included in this repository.** To download the relevant folder only:

```bash
git clone --filter=blob:none --sparse https://github.com/uoftcprg/phh-dataset.git
cd phh-dataset
git sparse-checkout set "data/handhq/PS-2009-07-01_2009-07-23_200NLH_OBFU"
```

## Requirements

- Python 3
- [PokerKit](https://github.com/uoftcprg/pokerkit)
- pandas

A full requirements file will be added later.

## Repository structure

To be added.

## Usage

To be added.

## Team

- Eesa Ghori
- Farhaan Soobratty

## References

- Kim, J. (2025). *A dataset of poker hand histories* (Version 3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.17136841
- Kim, J. (2025). PokerKit: A comprehensive Python library for fine-grained multivariant poker game simulations. *IEEE Transactions on Games*, 17(1), 32–39.

## Licence

To be confirmed. The underlying dataset is licensed under CC BY 4.0.
