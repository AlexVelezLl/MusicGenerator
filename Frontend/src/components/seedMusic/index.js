import React, { useState } from "react";

import MelodyPlayer from "../shared/MelodyPlayer";
import { modes, notes } from "../../constants";
import Select from "../shared/Select";
import { Slider, SliderThumbComponent } from "../shared/Slider";
import { transformMidiToMp3 } from "../../services";
// import bars from react-loader-spinner
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";
import { Bars } from "react-loader-spinner";

import "./index.css";
import { fontSize } from "@mui/system";

const SeedMusic = () => {
  const [temperature, setTemperature] = useState(20);
  const [currentAudio, setCurrentAudio] = useState(null);
  const [loading, setLoading] = useState(false);
  const handleTempSliderChange = (_, newValue) => {
    setTemperature(newValue);
  };
  const handleTempInputChange = (event) => {
    setTemperature(event.target.value === "" ? "" : Number(event.target.value));
  };
  const handleTempBlur = () => {
    if (temperature < 0) {
      setTemperature(0);
    } else if (temperature > 100) {
      setTemperature(100);
    }
  };

  const handleOnSubmit = async () => {
    setLoading(true);
    const input_midi = document.getElementById("input-midi").files[0];
    const url_file = await transformMidiToMp3(input_midi);
    setCurrentAudio(url_file);
    setLoading(false);
    console.log(currentAudio);
  };

  return (
    <section className="seed-music">
      <h2>Seed music</h2>

      <div className="seed-music-container">
        <div className="seed-music-options">
          <label htmlFor="input-midi" className="btn">
            <input id="input-midi" type="file" onChange={handleOnSubmit} />
            Select midi file
          </label>
          <div className="key-note">
            <div>
              <div className="label">Note:</div>
              <Select options={notes} defaultValue={notes[0]} />
            </div>
            <div>
              <div className="label">Mode:</div>
              <Select options={modes} defaultValue={modes[0]} />
            </div>
          </div>
          <div className="temperature-container">
            <div className="label">Temperature:</div>
            <div className="temperature">
              <Slider
                value={temperature}
                onChange={handleTempSliderChange}
                aria-labelledby="input-slider"
                components={{ Thumb: SliderThumbComponent }}
              />
              <input
                value={temperature}
                onChange={handleTempInputChange}
                onBlur={handleTempBlur}
                step={10}
                min={0}
                max={100}
                type="number"
                aria-labelledby="input-slider"
              />
            </div>
          </div>
        </div>
        <div className="seed-music-player">
          <div
            className="loader"
            style={{
              visibility: loading ? "visible" : "hidden",
            }}
          >
            <h2>Cargando audio...</h2>
            <div style={{ marginLeft: "40px" }}>
              <Bars
                color="#4CC678"
                height={100}
                width={100}

                visible={loading}
              />
            </div>
          </div>
          {currentAudio && !loading && <MelodyPlayer audio={currentAudio} />}
        </div>
      </div>
    </section>
  );
};

export default SeedMusic;
