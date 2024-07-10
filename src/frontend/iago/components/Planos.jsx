import { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import logo from '../assets/logo.svg';
import sobre from '../assets/sobre.png';

const Planos = () => {
  return (
    <div className='p-10 mt-10'>
      <h1 className='text-4xl'>
        Planos
      </h1>
      <div className="flex flex-wrap mt-14">
            <div class="flex-1 bg-gradient-to-r from-[#28009921] to-[#DB00FF30]  shadow-[#7000FF] shadow-md p-4 py-14 sm:mr-8 mb-8 mr-0 text-center rounded-3xl ">
            <h2 className='text-2xl text-[#FFE500]'>
                OURO          
            </h2>
            <p className='sm:px-14 mt-4 text-[#FFFFFF]'>
              Beneficios:
            </p>
            <button className="mt-10 bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#7000FF]">Iniciar
            </button>
            <p className='mt-8 text-3xl'>
            R$19,90/mês
            </p>
            </div>

            <div class="flex-1 bg-gradient-to-r from-[#FFFFFF43] to-[#6AF6FF71]  shadow-[#6AF6FF50] shadow-lg p-4 py-14 text-center rounded-3xl mb-8">
            <h2 className='text-2xl'>
                PRATA          
            </h2>
            <p className='sm:px-14 mt-4 text-[#FFFFFF]'>
              Beneficios:
            </p>
            <button className="mt-10 bg-gradient-to-r from-[#7000FF] to-[#00F0FF50] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#00F0FF]">Iniciar
            </button>
            <p className='mt-8 text-[#00F0FF] text-2xl'>
                RECOMENDADO
            </p>
            <p className='mt-8 text-3xl'>
              R$19,90/mês            
            </p>
            </div>

            <div class="flex-1 bg-gradient-to-r from-[#28009921] to-[#DB00FF30]  shadow-[#7000FF] shadow-md p-4 py-14 sm:ml-8 mb-8 text-center rounded-3xl ">
            <h2 className='text-2xl text-[#FFBE73]'>
              BRONZE          
            </h2>
            <p className='sm:px-14 mt-4 text-[#FFFFFF]'>
            Beneficios:
            </p>
            <button className="mt-10 bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#7000FF]">Iniciar
            </button>
            <p className='mt-8 text-3xl'>
              R$19,90/mês            
            </p>
            </div>
    </div>

    </div>
  );
};

export default Planos;
