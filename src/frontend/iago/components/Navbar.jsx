// components/Navbar.jsx

import { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import logo from '../assets/logo.svg';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="p-4 fixed w-full z-50 font-text">
      <div className="flex justify-between items-center">
        <div className="flex-1">
          <Link href="/">
            <Image src={logo} alt="Logo" width={180} height={180} />
          </Link>
        </div>
        <div className="md:flex hidden flex-1 justify-around text-white font-light text-lg">
          <Link href="/" className='hover:text-purple-500'>Menu</Link>
          <Link href="/ourpurpose" className='hover:text-purple-500'>Serviços</Link>
          <Link href="/partners" className='hover:text-purple-500'>Contato</Link>
          <Link href="/media" className='hover:text-purple-500'>Sobre</Link>
          <Link href="/contactus" className='hover:text-purple-500'>Planos</Link>
          <Link href="/contactus" className='text-purple-500 font-bold text-xl'>Cadastrar</Link>

        </div>
        <button className="text-white md:hidden" onClick={() => setIsOpen(!isOpen)}>
          {isOpen ? '✖' : '☰'}
        </button>
      </div>
      {isOpen && (
        <div className="flex flex-col items-center md:hidden bg-black bg-opacity-80">
          <Link href="/"><p className="text-white py-2">Menu</p></Link>
          <Link href="/ourpurpose"><p className="text-white py-2">Serviços</p></Link>
          <Link href="/partners"><p className="text-white py-2">Contato</p></Link>
          <Link href="/media"><p className="text-white py-2">Sobre</p></Link>
          <Link href="/contactus"><p className="text-white py-2">Planos</p></Link>
          <Link href="/contactus"><p className="text-purple-500 font-bold px-4 py-2 rounded-md text-sm">Cadastrar</p></Link>

        </div>
      )}
    </nav>
  );
};

export default Navbar;
