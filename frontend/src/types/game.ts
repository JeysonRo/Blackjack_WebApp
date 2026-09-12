export type GameState = {
    "dealer_hand": string[];
    "player_hands": string[][];
    "finished_hands": string[][];
    "valid_actions": string[];
}

export type Action = "hit" | "stand" | "double" | "split" | "surrender";

export type GameSettings = {
    "dealer_behavior": "H17" | "S17";
    "surrender_enabled": boolean;
}