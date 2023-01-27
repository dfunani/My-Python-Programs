import Head from 'next/head'
import { Inter } from '@next/font/google'
import styles from '../styles/Home.module.css'
import TeamCard from './components/TeamCard'
import Header from './components/Header'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
      <Header club={{}} name="England"/>
      <TeamCard club={{}} />
    </>
  )
}
