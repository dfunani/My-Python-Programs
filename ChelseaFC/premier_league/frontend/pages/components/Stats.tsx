import Image from "next/image"
import logo from '../../public/next.svg'
import styles from '../../styles/Stats.module.css'
type props = {
	results: object;
}

export default function Stats({ results }: props)
{
	return (
		<div className={styles.Container}>
			<div className={styles.Match_1}>
				<div className={styles.Pill}>
					<div></div>
					<div></div>
				</div>
			</div>
		</div>
	)
}