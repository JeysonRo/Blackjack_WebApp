import type { GameSettings, GameState } from "../types/game";

// const API_URL = import.meta.env.PROD
//     ? import.meta.env.VITE_API_URL
//     : "";

const apiUrl = (path: string) => path;

export async function getGameState() {
    const response = await fetch(apiUrl("/api/game"), {
        credentials: "include",
        method: "GET",
    });

    if (!response.ok) {
        throw new Error("Failed to fetch game");
    }

    return response.json();
}

export async function startGame(settings: GameSettings): Promise<GameState> {
    const response = await fetch(apiUrl("/api/game"), {
        credentials: "include",
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ settings }),
    });

    if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
    }

    return response.json();
}

export async function chooseAction(action: string): Promise<GameState> {
    const response = await fetch(apiUrl("/api/game/action"), {
        credentials: "include",
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ action }),
    });

    if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
    }

    return response.json();
}