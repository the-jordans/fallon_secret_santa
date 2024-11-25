import { family, Name, Person, YEARS_THIS_CYCLE } from "./data"
import { Result } from "./hat"

export const resultsAreValid = (results: Array<Result>) =>
    results.every(result => resultIsValid(result)) &&
    noDuplicateReceivers(results) &&
    everyoneIsAccountedFor(results)

const resultIsValid = ({ santa, receiver }: Result) =>
    notTheSamePerson(receiver, santa) &&
    notTheirSigOther(receiver, santa) &&
    haventGottenThemThisCycle(receiver, santa)

const notTheSamePerson = (receiver: Name, santa: Person) =>
    receiver != santa.name

const notTheirSigOther = (receiver: Name, santa: Person) =>
    receiver != santa.sigOther

const haventGottenThemThisCycle = (receiver: Name, santa: Person) =>
    YEARS_THIS_CYCLE.map(year => santa.history[year])
        .indexOf(receiver) == -1

const noDuplicateReceivers = (results: Array<Result>) =>
    new Set(results.map(result => result.receiver)).size == results.length

const everyoneIsAccountedFor = (results: Array<Result>) =>
    family.every(person => results.map(result => result.receiver).indexOf(person.name) != -1)
