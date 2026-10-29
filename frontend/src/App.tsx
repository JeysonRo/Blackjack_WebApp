import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { chooseAction, getGameState, startGame } from "./api/game";
import { useEffect, useState } from "react";
import "./App.css"
import Actions from "./components/Actions"
import Menu from "./components/Menu";
import Players from "./components/Players";
import Hand from "./components/Hand";
import Settings from "./components/Settings";
import type { GameSettings } from "./types/game";

function App() {
  const [settingsOpen, setSettingsOpen] = useState(false);
  const [settings, setSettings] = useState<GameSettings>(() => {
    const saved = localStorage.getItem("gameSettings");
    if (saved) {
      return JSON.parse(saved);
    } else {
      return {
        dealer_behavior: "H17",
        surrender_enabled: false,
      };
    }
  });

  useEffect(() => {
    localStorage.setItem(
      "gameSettings",
      JSON.stringify(settings)
    );
  }, [settings]);

  const queryClient = useQueryClient();

  const gameStateQuery = useQuery({
    queryKey: ["game"],
    queryFn: getGameState,
  });

  const startGameMutation = useMutation({
    mutationFn: startGame,
    onSuccess: (data) => {
      queryClient.setQueryData(["game"], data);
    },
  });

  const actionMutation = useMutation({
    mutationFn: chooseAction,
    onSuccess: (data) => {
      queryClient.setQueryData(["game"], data);
    },
  });

  return (
    <div className="App">
      <header>
        <h1>Blackjack</h1>
      </header>

      <button className="settings-button" onClick={() => setSettingsOpen(true)}>Settings</button>
      {settingsOpen && (
        <div className="settings-panel">
          <button onClick={() => setSettingsOpen(false)}>✕</button>
          <h2>Settings</h2>

          <Settings settings={settings} setSettings={setSettings}/>

        </div>
      )}

      <main>
        <Menu startGameMutation={startGameMutation} settings={settings} />

        <section className="dealer">
          <h2>Dealer</h2>
          {gameStateQuery.data && (
            <Hand cards={gameStateQuery.data.dealer_hand}/>
          )}
        </section>

        <Players gameState={gameStateQuery.data}/>
        
        {gameStateQuery.data && (
          <Actions gameState={gameStateQuery.data} actionMutation={actionMutation} /> /* component to show actions */
        )}
      </main>
    </div>
  );
}

export default App;