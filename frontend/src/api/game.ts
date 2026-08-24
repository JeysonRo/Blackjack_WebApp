import type { GameState } from "../types/game";

export async function getGame() {
    const response = await fetch("/api/game");

    if (!response.ok) {
        throw new Error("Failed to fetch game");
    }

    return response.json();
}

export async function startGame(): Promise<GameState> {
    const response = await fetch("/api/game", {
        method: "POST",
    });

    if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
    }

    return response.json();
}