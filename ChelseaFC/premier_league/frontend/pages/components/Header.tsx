import styles from '../../styles/Header.module.css'

type props = {
	name: string;
	club: object;
}

export default function Header({ club, name }: props)
{
	return (
		<div className={styles.Container}>
			<button>=</button>
			<h1 className={ styles.Name}>{ name }</h1>
		</div>
	)
}