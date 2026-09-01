export type GameState = {
    "dealer_hand": string[];
    "player_hands": string[][];
    "finished_hands": string[][];
    "valid_actions": string[];
}

export type Action = "hit" | "stand" | "double" | "split" | "surrender";