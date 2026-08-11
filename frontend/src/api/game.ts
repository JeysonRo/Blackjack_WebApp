export async function getGame() {
    const response = await fetch("/api/game");

    if (!response.ok) {
        throw new Error("Failed to fetch game");
    }

    return response.json();
}