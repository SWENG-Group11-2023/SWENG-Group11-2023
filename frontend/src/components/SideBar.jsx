import React ,{useState} from 'react'
import {
  FaRegChartBar,
  FaTh,
  FaBars
} from "react-icons/fa";
import { NavLink } from 'react-router-dom';

const SideBar= ({children}) => {
  const [isOpen ,setIsOpen] = useState(false);
  const toggle = () => setIsOpen (!isOpen);
  const menuItem=[
    {
      path: "/",
      name: "Dashboard",
      icon:<FaTh/>
    },
    {
      path: "/analytics",
      name: "Analytics",
      icon:<FaRegChartBar/>
    },
  ]
  return (
    <div className="container">
      <div style={{width:isOpen ? "300px" : "50px"}}className="SideBar">
        <div className="top_section">
          <h1 style={{display:isOpen ? "block" : "none"}}className="logo">Logo</h1>
          <div style={{marginLeft:isOpen ? "50px" : "0px"}}className="bars">
            <FaBars onClick={toggle}/>
          </div>
        </div>
        {
          menuItem.map((item,index)=> (
            <NavLink to={item.path} key={index} className="link" activeclassName="active">
              <div className="icon">{item.icon}</div>
              <div style={{display:isOpen ? "block" : "none"}}className="link_text">{item.name}</div>
            </NavLink>
          ))
        }
      </div>
        <main>{children}</main>
    </div>
  );
};
export default SideBar;