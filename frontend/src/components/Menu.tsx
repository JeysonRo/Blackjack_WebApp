import type { UseMutationResult } from "@tanstack/react-query"
import type { GameState } from "../types/game";

type Props = {
  startGameMutation: UseMutationResult<GameState, Error, void, unknown>;
};

export default function Menu({ startGameMutation }: Props ){
    return (
        <div className="Menu">
          <button
           onClick={() => startGameMutation.mutate()}
           disabled={startGameMutation.isPending}
           >
            {startGameMutation.isPending ? "Starting..." : "Start Game"}
          </button>

          {startGameMutation.isError && (
            <p>Error: {startGameMutation.error.message}</p>
          )}
        </div>
    )
}