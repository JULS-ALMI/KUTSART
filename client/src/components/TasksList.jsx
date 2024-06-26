import { useEffect } from "react";
import { getAllTasks } from "../api/tasks.api";
import React, { useState } from 'react';

export function TasksList() {

useEffect(() => {
  function loadtasks() {
    const res = getAllTasks();
      console.log(res);
  }
  loadtasks();
}, []);

  return <div>Prueba</div>;
  
};

