/*************************************************
 EDUCATIONAL DEMO: PT ADAPTIVE EXERCISE APP
 NOT FOR MEDICAL USE
*************************************************/

import React, { useState } from 'react';
import { View, Text, TextInput, Button, TouchableOpacity } from 'react-native';

/***********************
 SIMPLE NAVIGATION STATE
***********************/
export default function App() {
  const [screen, setScreen] = useState("login");

  const [user, setUser] = useState({
    email: "",
    age: "",
    gender: "",
    complaint: "",
    painArea: ""
  });

  const [baselinePain, setBaselinePain] = useState(0);
  const [assessmentResult, setAssessmentResult] = useState([]);
  const [currentExerciseIndex, setCurrentExerciseIndex] = useState(0);
  const [difficulty, setDifficulty] = useState("");
  const [painResponse, setPainResponse] = useState("");

  /***********************
  MOCK EXERCISE DATABASE
  ***********************/
  const exerciseLibrary = [
    { name: "Glute Bridge", muscle: "glutes" },
    { name: "Quad Set", muscle: "quadriceps" },
    { name: "Standing Hip Abduction", muscle: "hip abductors" },
    { name: "Heel Raises", muscle: "calves" },
    { name: "Core Marching", muscle: "core" }
  ];

  /***********************
  PROGRESSION LOGIC
  ***********************/
  function decideProgression(pain, difficulty) {
    if (pain === "increased") return "regress";
    if (pain !== "increased" && difficulty === "easy") return "progress";
    if (difficulty === "just right") return "keep";
    return "keep";
  }

  /***********************
  SCREENS
  ***********************/
  if (screen === "login") {
    return (
      <View>
        <Text>Login (Educational)</Text>
        <TextInput placeholder="Email" />
        <TextInput placeholder="Password" secureTextEntry />
        <Button title="Login" onPress={() => setScreen("demographics")} />
      </View>
    );
  }

  if (screen === "demographics") {
    return (
      <View>
        <Text>Demographics</Text>

        <TextInput
          placeholder="Age"
          keyboardType="numeric"
          onChangeText={(text) => setUser({ ...user, age: text })}
        />

        <Button title="Female" onPress={() => setUser({ ...user, gender: "female" })} />
        <Button title="Male" onPress={() => setUser({ ...user, gender: "male" })} />

        <Button title="Pain" onPress={() => setUser({ ...user, complaint: "pain" })} />
        <Button title="Balance" onPress={() => setUser({ ...user, complaint: "balance" })} />

        <Button title="Continue" onPress={() => setScreen("assessment")} />
      </View>
    );
  }

  if (screen === "assessment") {
    return (
      <View>
        <Text>Movement Assessment (Educational)</Text>
        <Text>Walking</Text>
        <Text>Squat</Text>
        <Text>Single Leg Balance</Text>

        <Button
          title="Assessment Complete"
          onPress={() => {
            setAssessmentResult(["glutes", "quadriceps"]);
            setScreen("baselinePain");
          }}
        />
      </View>
    );
  }

  if (screen === "baselinePain") {
    return (
      <View>
        <Text>Baseline Pain (0–10)</Text>
        <TextInput
          keyboardType="numeric"
          onChangeText={(text) => setBaselinePain(Number(text))}
        />
        <Button title="Start Exercises" onPress={() => setScreen("exercise")} />
      </View>
    );
  }

  if (screen === "exercise") {
    const exercise = exerciseLibrary[currentExerciseIndex];

    return (
      <View>
        <Text>Exercise {currentExerciseIndex + 1} of 5</Text>
        <Text>{exercise.name}</Text>
        <Text>Target: {exercise.muscle}</Text>

        <Text>Difficulty</Text>
        <Button title="Easy" onPress={() => setDifficulty("easy")} />
        <Button title="Just Right" onPress={() => setDifficulty("just right")} />
        <Button title="Hard" onPress={() => setDifficulty("hard")} />

        <Text>Pain Response</Text>
        <Button title="Same" onPress={() => setPainResponse("same")} />
        <Button title="Increased" onPress={() => setPainResponse("increased")} />

        <Button
          title="Next Exercise"
          onPress={() => {
            const decision = decideProgression(painResponse, difficulty);
            console.log("Decision:", decision);

            if (currentExerciseIndex < 4) {
              setCurrentExerciseIndex(currentExerciseIndex + 1);
            } else {
              setScreen("postPain");
            }
          }}
        />
      </View>
    );
  }

  if (screen === "postPain") {
    return (
      <View>
        <Text>Post-Session Pain</Text>
        <TextInput keyboardType="numeric" />
        <Button title="Finish Session" onPress={() => setScreen("done")} />
      </View>
    );
  }

  if (screen === "done") {
    return (
      <View>
        <Text>Session Complete</Text>
        <Text>Exercises will adapt next session.</Text>
      </View>
    );
  }

  return null;
}
