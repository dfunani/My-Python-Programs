import styles from '../../styles/TeamCard.module.css'
import data from '../api/static'
import Stats from './Stats'
type props = {
	club: object;
}

export default function TeamCard({club}: props)
{
	return (
		<div className={styles.Container}>
			<div className={styles.Bio}>
				<p>
					{data}
				</p>
			</div>
			<div className={styles.Stats}>
				<div className={styles.Results}>
					<Stats results={{}} />
				</div>
				<div className={styles.Fixtures}>
					<Stats results={{}} />
				</div>
				<div className={styles.Standings}>
					<Stats results={{}} />
				</div>
				<div className={styles.Trophies}>
					<Stats results={{}} />
				</div>
			</div>
			
		</div>
	)
}
