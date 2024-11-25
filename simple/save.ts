import { writeFileSync } from "fs"
import { SimpleResult } from "./hat"
import { Name } from "./data"


export const saveToFiles = (results: Array<SimpleResult>) => {
    const fallonSanta = theirSanta('Jordan Fallon', results)
    const haganSanta = theirSanta('Jordan Hagan', results)
    const theRest = results.filter(result => result.santa != fallonSanta.santa && result.santa != haganSanta.santa)
    const midpoint = Math.ceil(theRest.length/2)

    const fallonNotes = makeNotes([haganSanta].concat(theRest.slice(0, midpoint)))
    const haganNotes = makeNotes([fallonSanta].concat(theRest.slice(midpoint)))

    writeFileSync("fallon.txt", fallonNotes)
    writeFileSync("hagan.txt", haganNotes)
}

const theirSanta = (name: Name, results: Array<SimpleResult>) =>
    results.filter(result => result.receiver == name)[0]

const makeNotes = (list: Array<SimpleResult>) =>
    list.map(result => `${result.santa} is getting a gift for ${result.receiver}`)
        .join('\n')
