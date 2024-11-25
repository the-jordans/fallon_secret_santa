import { family, Name, Person } from "./data"
import { resultsAreValid } from "./validator"

export type Result = {
    santa: Person
    receiver: Name
}

export type SimpleResult = {
    santa: Name
    receiver: Name
}

export const drawNames = () => {
    const familyNames = family.map(person => person.name)
    while (true) {
        const results = family.map(person => {
            const name = drawNameFor(person, familyNames)
            return { santa: person, receiver: name }
        })

        if (resultsAreValid(results))
            return results.map(({ santa, receiver }) => ({ santa: santa.name, receiver }))
    }
}

const drawNameFor = (person: Person, familyNames: Array<Name>) => {
    const options = familyNames.filter(name => name != person.name && name != person.sigOther)
    return options[Math.floor(Math.random() * options.length)]
}
