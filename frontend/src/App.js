///import {DataFetching} from './pages/DataFetching';
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Analytics from './pages/Analytics';
import SideBar from './components/SideBar';
import Navbar from './components/Navbar';
import React from 'react';
import Group from './pages/Group';
import Clients from './pages/Clients';
import Project from './pages/Project';


const App = () => {
  return (
    <BrowserRouter>
    <React.Fragment>
      <Navbar/>
    </React.Fragment>
    <SideBar>
    <Routes>
      <Route path ="/"element={<Dashboard/>}/>
      <Route path ="/dashboard"element={<Dashboard/>}/>
      <Route path ="/analytics"element={<Analytics/>}/>
      <Route path ="/Group"element={<Group/>}/>
      <Route path ="/Clients"element={<Clients/>}/>
      <Route path ="/Project"element={<Project/>}/>
    </Routes>
    </SideBar>
    </BrowserRouter>
  );
};
export default  App;