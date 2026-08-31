export type GameState = {
    "dealer_hand": string[];
    "player_hand": string[];
    "valid_actions": string[];
}

export type Action = "hit" | "stand" | "double" | "split" | "surrender";