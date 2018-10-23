# UK Biobank Self Reported Medication Data parsing and matching

## NOTE: ## this repository is superseded by: [../ukbb-srmed](UKBB-srmed)

## Overview
Code to match UK biobank (UKBB) Self-Reported Medication (SRMed) descriptions with descriptions from a classification system. Data from the Anatomical Therapeutic Chemical (ATC) classification system defined by the WHO and code data from the British National Formulary (BNF) have been tested against during development.

The objective is to provide the means to classify UKBB Self-Reported medication data into related therapy groups for the purpose of enabling additional evidence from UKBB phenotype data to be collected when deriving both individual clinical phenotypes (Asthma, Neuropathic Pain, T2 Diabetes) and when generating a range of phenotypes for Phenome Wide Association Studies (PhewAS). 

## Description
Matching code is written in Python 2 (2.7 was used for development). Extensive use of Bash shell wrappers is made to supply context:- Data directory locations, data file names, database access parameters ...

> ### Subdirectories:

> *env* Environment variables used are shown in a single file 'common_tplt', users should complete these and copy to a file named 'common', users must also pre-define **PROJDATA** and **PROJROOT**. Parameters for local chembl database access are also required for drug synonym extraction.

> *py* Python scripts, including the module 'datahelper.py' which is where the text matching code is to be found.

> *sh* Bash shell scripts, wrappers for the python code split into several main functions and provided for coding against the ATC classification system (BNF-specific sh scripts to follow).

