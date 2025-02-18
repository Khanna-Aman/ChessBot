# ChessBot - FIDE & Google Efficient Chess AI Challenge

This repository contains a **ChessBot** designed for the **FIDE & Google Efficient Chess AI Challenge** on Kaggle. The bot is optimized for fast decision-making and minimal memory usage within the constraints set by the competition.

## Challenge Overview
The **FIDE & Google Efficient Chess AI Challenge** on Kaggle focuses on creating a fast and efficient chess-playing bot that can make decisions within very limited computational resources:
- **5 MiB RAM**
- **2.20 GHz single CPU core**
- **64 KiB compressed submission size**
- **10s per game with 0.1s simple delay**

The bot plays chess by using a **simple evaluation function**, prioritizing:
- Checkmate
- Material gain (capturing valuable pieces)

## Features
- Efficient move selection strategy based on checkmate and material evaluation.
- Fast decision-making with minimal computational resources.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/Khanna-Aman/ChessBot.git
