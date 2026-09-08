import type { UseMutationResult } from "@tanstack/react-query"
import type { GameState } from "../types/game";

type Props = {
  gameState: GameState | undefined;
  actionMutation: UseMutationResult<GameState, Error, string, unknown>;
};

export default function Actions({gameState, actionMutation}: Props) {
    return (
        <div className="button-group">
          {/* {gameState?.valid_actions?.includes("continue") && (<button className="button" onClick={() => actionMutation.mutate("stand")}>Continue</button>)} */}
          {gameState?.valid_actions?.includes("hit") && (<button className="button" onClick={() => actionMutation.mutate("hit")}>Hit</button>)}
          {gameState?.valid_actions?.includes("stand") && (<button className="button" onClick={() => actionMutation.mutate("stand")}>Stand</button>)}
          {gameState?.valid_actions?.includes("double") && (<button className="button" onClick={() => actionMutation.mutate("double")}>Double</button>)}
          {gameState?.valid_actions?.includes("split") && (<button className="button" onClick={() => actionMutation.mutate("split")}>Split</button>)}
          {/* {gameState?.valid_actions?.includes("surrender") && (<button className="button" onClick={() => actionMutation.mutate("surrender")}>Surrender</button>)} */}
        </div>
    );
}
