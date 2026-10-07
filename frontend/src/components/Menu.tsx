import type { UseMutationResult } from "@tanstack/react-query"
import type { GameSettings, GameState } from "../types/game";

type Props = {
  startGameMutation: UseMutationResult<GameState, Error, GameSettings, unknown>;
  settings: GameSettings;
};

export default function Menu({ startGameMutation, settings }: Props ){
    return (
        <div className="Menu">
          <button className="button"
           onClick={() => startGameMutation.mutate(settings)}
           disabled={startGameMutation.isPending}
           >
            {startGameMutation.isPending ? "Starting..." : "Start New Game"}
          </button>

          {startGameMutation.isError && (
            <p>Error: {startGameMutation.error.message}</p>
          )}
        </div>
    )
}