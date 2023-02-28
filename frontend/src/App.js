///import {DataFetching} from './pages/DataFetching';
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Analytics from './pages/Analytics';
import SideBar from './components/SideBar';

const App = () => {
  return (
    <BrowserRouter>
    <SideBar>
    <Routes>
      <Route path ="/"element={<Dashboard/>}/>
      <Route path ="/dashboard"element={<Dashboard/>}/>
      <Route path ="/analytics"element={<Analytics/>}/>
    </Routes>
    </SideBar>
    </BrowserRouter>
  );
};
export default  App;