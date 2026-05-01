---
title: "DLL Preloading Attack"
date: 2026-04-30
type: permanent
category: "Computer Science/Security"
tags: [security, windows, vulnerabilities]
status: draft
related: ["[[Elevation of Privilege]]", "[[Security Vulnerabilities]]", "[[STRIDE]]"]
---

# DLL Preloading Attack

A DLL preloading attack abuses the order Windows uses when resolving a dynamic-link library by name.

If an application loads a DLL without a fully qualified path, the operating system searches multiple directories for a matching library. An attacker can place a malicious DLL earlier in that search path so the application loads attacker-controlled code instead of the intended dependency.

The important design lesson is that dependency resolution is part of the trust boundary. Applications should load libraries from explicit trusted paths, avoid unsafe current-directory lookup, and treat dependency loading as a possible [[Elevation of Privilege]] path.

## Related

- [[Elevation of Privilege]]
- [[Security Vulnerabilities]]
- [[STRIDE]]
