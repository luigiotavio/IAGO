import { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import logo from '../assets/logo.svg';

const Ferramentas = () => {

  return (

    <div className='p-10'>
        <h1 className="text-4xl">
            Serviços <span className="text-purple-600">IAGO</span>!
        </h1>

        <div className="flex flex-wrap mt-10">
            <div class="flex-1 bg-gradient-to-r from-[#28009921] to-[#DB00FF30]  shadow-[#7000FF] shadow-md p-4 py-14 sm:mr-8 mb-8 mr-0 text-center rounded-3xl ">
            <h2 className='text-2xl'>
                Chatbot especializado          </h2>
            <p className='sm:px-14 mt-4 text-[#FFFFFF43]'>
                Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.          
            </p>
            <button className="mt-10 bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#7000FF]">Iniciar
            </button>
            </div>

            <div class="flex-1 bg-gradient-to-r from-[#FFFFFF43] to-[#6AF6FF71]  shadow-[#6AF6FF50] shadow-lg p-4 py-14 text-center rounded-3xl mb-8">
            <h2 className='text-2xl'>
                Chatbot especializado          </h2>
            <p className='sm:px-14 mt-4 text-[#FFFFFF]'>
                Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.          
            </p>
            <button className="mt-10 bg-gradient-to-r from-[#7000FF] to-[#00F0FF50] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#00F0FF]">Iniciar
            </button>
            <p className='mt-8 text-[#00F0FF] text-2xl'>
                POPULAR
            </p>
            </div>

            <div class="flex-1 bg-gradient-to-r from-[#28009921] to-[#DB00FF30]  shadow-[#7000FF] shadow-md p-4 py-14 sm:ml-8 mb-8 text-center rounded-3xl ">
            <h2 className='text-2xl'>
                Chatbot especializado          </h2>
            <p className='sm:px-14 mt-4 text-[#FFFFFF43]'>
                Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.          
            </p>
            <button className="mt-10 bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#7000FF]">Iniciar
            </button>
            </div>



        </div>
    </div>

  );
};

export default Ferramentas;
