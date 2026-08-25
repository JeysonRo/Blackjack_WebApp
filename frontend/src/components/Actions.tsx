import type { UseMutationResult } from "@tanstack/react-query"
import type { GameState } from "../types/game";

type Props = {
  startGameMutation: UseMutationResult<GameState, Error, void, unknown>;
};

export default function Actions({startGameMutation}: Props) {
    return (
        <div className="actions">
          {startGameMutation.data?.valid_actions.includes("hit") && (<button>Hit</button>)}
          {startGameMutation.data?.valid_actions.includes("stand") && (<button>Stand</button>)}
          {startGameMutation.data?.valid_actions.includes("double") && (<button>Double</button>)}
          {startGameMutation.data?.valid_actions.includes("split") && (<button>Split</button>)}
        </div>
    );
}
