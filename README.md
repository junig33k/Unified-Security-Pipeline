# Unified Security Pipeline

![Security Pipeline](https://github.com/junig33k/Unified-Security-Pipeline/actions/workflows/ci.yml/badge.svg)

Pipeline DevSecOps intégrant une architecture modulaire pour l'automatisation des analyses de sécurité et de mutation de payloads.

## Composants
- **Dork Scanner** : Analyse de cibles et collecte.
- **Payload Mutator** : Génération et transformation de vecteurs.
- **Orchestrator** : Pipeline principal d'exécution.

## Sécurité & Qualité (CI/CD)
- Linting : `flake8`
- SAST (Static Application Security Testing) : `bandit`
