import type { GameSettings } from "../types/game";

interface SettingsProps {
    settings: GameSettings;
    setSettings: React.Dispatch<React.SetStateAction<GameSettings>>;
}

export default function Settings({settings, setSettings,}: SettingsProps) {
    return (
    <div className="setting">
        <span>Dealer hits soft 17</span>

        <button
        className={`toggle ${settings.dealer_behavior === "H17" ? "active" : ""}`}
        onClick={() => 
            setSettings(prev => ({
                ...prev,
                dealer_behavior: prev.dealer_behavior === "H17" ? "S17" : "H17",
            }))
        }
        >
        <span className="toggle-knob" />
        </button>

        <span>{settings.dealer_behavior}</span>
    </div>
    );
}