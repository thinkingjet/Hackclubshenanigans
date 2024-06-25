import { ReactMediaRecorder } from "react-media-recorder";
import RecordIcon from "./RecordIcon";

type Props = {
  handleStop: any;
};

// RecordMessage component to handle recording of audio messages
const RecordMessage = ({ handleStop }: Props) => {
  return (
    // ReactMediaRecorder is a component that facilitates media recording
    <ReactMediaRecorder
      audio
      // onStop is a callback function that is called when the recording stops
      onStop={handleStop}
      // render is a render prop that returns UI based on the recording status
      render={({ status, startRecording, stopRecording }) => (
        <div className="mt-2">
          {/* Button to start and stop recording */}
          {/* The recording starts on mouse down and stops on mouse up */}
          <button
            onMouseDown={startRecording}
            onMouseUp={stopRecording}
            className="bg-black p-4 rounded-full"
          >
            {/* RecordIcon component displays a recording icon */}
            {/* The icon color changes based on the recording status */}
            {/* When recording, the icon pulsates with a red color */}
            {/* When not recording, the icon is sky blue */}
            <RecordIcon
              classText={
                status == "recording"
                  ? "animate-pulse text-red-500"
                  : "text-sky-500"
              }
            />
          </button>
          {/* Display the current status of the recording */}
          {/* The status can be 'idle', 'recording', or 'stopped' */}
          <p className="mt-2 text-white font-light">{status}</p>
        </div>
      )}
    />
  );
};

export default RecordMessage;
