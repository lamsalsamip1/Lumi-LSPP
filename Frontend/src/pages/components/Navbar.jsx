
import { Link } from 'react-router-dom';
import { lumi, menu, close } from '../../assets'
import { navLinks } from '../../constants'
import { useState } from 'react';


const Navbar = () => {
    const [toggle, setToggle] = useState(false)

    return (
        <nav
            className={` w-full flex items-center py-2 fixed top-0 z-20 bg-navbg shadow-md `}
        >
            <div className="w-full flex justify-between items-center max-w-7xl mx-auto">
                <div className='flex gap-3'>
                    <Link to="/"
                        className='flex items-center gap-2'
                        onClick={() => {
                            window.scrollTo(0, 0)
                        }
                        }
                    >
                        <img src={lumi} alt="logo" className='w-16 h-16 object-contain' />

                    </Link>
                </div>


                <ul className='list-none hidden sm:flex flex-row gap-10'>
                    {navLinks.map((link) => {
                        return (
                            <li
                                key={link.id}
                                className="text-graytext hover:text-black text-[18px] font-medium cursor-pointer"
                                >
                                <a href={`${link.id}`}>{link.title}</a>
                            </li>
                        )
                    })}
                </ul>


                <div className='sm:hidden flex-flex-1 justify-end items-center py-2 mx-2'>
                    <img
                        src={toggle ? close : menu}
                        alt="menu"
                        className='w-[28px] h-[28px] object-contain cursor-pointer'
                        onClick={() => setToggle(!toggle)}
                    />

                    <div className={`${!toggle ? "hidden" : "flex"} p-6 black-gradient absolute top-20 right-0 mx-4 my-2 min-w-[140px] z-10 rounded-xl`} >
                        <ul className='list-none flex justify-end items-start flex-col gap-4'>

                            {navLinks.map((link) => {
                                return (
                                    <li
                                        key={link.id}
                                        className="text-graytext ont-medium cursor-pointer text-[16px]"
                                        onClick={() => {
                                            setToggle(!toggle);
                                        }}>
                                        <a href={`${link.id}`}>{link.title}</a>
                                    </li>
                                )
                            })}
                        </ul>
                    </div>

                </div>
            </div>
        </nav>
    )
}

export default Navbar
