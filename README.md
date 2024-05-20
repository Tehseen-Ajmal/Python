# Transliterater

## Introduction

This project is a Python-based transliterator that converts text between Urdu and Roman Urdu. It supports transliterating entire sentences, not just single words. This tool is particularly useful for converting double letters with single sounds such as `kh`, `ch`, `th`, `dh`, `gh`, `xh`, `sh`, `bh`, `ph`, etc.

The transliterator uses customizable rules to handle various transliteration patterns, ensuring accurate and readable conversions. It addresses common challenges in transliteration, such as variations in spelling and pronunciation, and provides a reliable way to convert text between these scripts. This project can be especially useful for those who need to switch between Urdu and Roman Urdu frequently and seek an efficient and effective solution for their transliteration needs.

## Features

- **Roman Urdu to Urdu Transliteration**
- **Urdu to Roman Urdu Transliteration**
- **Sentence-level Transliteration**
- **Special Handling for Double Letters with Single Sounds**
- **Customizable Transliteration Rules**

## Sample Words and Results

| Roman Urdu Text                              | Urdu Text                          |
|----------------------------------------------|------------------------------------|
| Tehseen                                      | تحسیں                                |
| Haathi                                       | ہاتھی                                |
| Doodh                                        | دودھ                                 |
| Shukria                                      | شُکریا                                |
| Ghazal                                       | غَزَل                                 |
| Khaalid                                      | خالد                                 |
| Kahaan gai thay                              | کَہاں گے تھے                           |

## Rules for English/Roman Urdu

- Use `aa` for `ا` like `khaalid` for خالد.
- Use `xh` for `چھ` and follow the sample phrases provided for best results.

## Important Information for Urdu

- This program works perfectly with Aeraab (اعراب).

## Usage

To use the transliterator, enter text in Urdu with Aeraabs or in Roman Urdu. Use `aa` for `ا` between words, like `khaana` (کھانا), `khaalid` (خالد), `khaan` (خان), and single `a` at the start or end like `ali` (علی), `axha` (اچھا).
