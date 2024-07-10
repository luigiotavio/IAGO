import Banner from "@components/Banner"
import Navbar from "@components/Navbar"
import Servicos from "@components/Servicos"
import Ferramentas from "@components/Ferramentas"
import Sobre from "@components/Sobre"
import Planos from "@components/Planos"
import Footer from "@components/Footer"

export default function Home() {
  return (
    <div className="bg-[#3A338E20]">
      <Navbar />
      <Banner />
      <Servicos />
      <Ferramentas />
      <Sobre />
      <Planos />
      <Footer />

    </div>
  )
}
