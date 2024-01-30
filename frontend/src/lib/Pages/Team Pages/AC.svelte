<script lang ='ts'>
    import Banner from '../../Components/Banner.svelte';
    import NavBar from "../../Components/NavBar.svelte";
    import GroupSection from "../../Components/GroupSection.svelte";
    import ICJ from "../../../assets/AC/ICJ/ICJ.jpg"
    import HRC from "../../../assets/AC/HRC.png"
    import GA from "../../../assets/AC/GA.jpg"
    import ECOSOC from "../../../assets/AC/ECOSOC.jpg"
    import SC from "../../../assets/AC/SC/SC.jpg"
    import JC from "../../../assets/AC/JC/JC.jpg"
</script>

<NavBar />

<Banner />

<main class="grid grid-flow-row grid-cols-1 space-y-5 m-5">
    <GroupSection noReadMe={false} header="International Court of Justice" link="/meet/ac/ICJ" text={null} image={ICJ} />
    <GroupSection noReadMe={false} header="Human Rights Council" link="/meet/ac/HRC" text={"The Human Rights Council is crucial for promoting global peace and justice whilst holding nations accountable for the rights they are violating. This council functions according to values such as fairness, inclusion and justice. By joining this committee, delegates can demonstrate their belief in human rights, have meaningful discussions and shape the international standard. It also encourages cooperation in achieving the goal of a more just world as it emphasises the protection and promotion of rights world wide. Join HRC to solve global issues and help those in need. Give a voice to those who have never been heard."} image={HRC} />
    <GroupSection noReadMe={false} header="General Assembly" link = "/meet/ac/GA" text={null} image={GA} />
    <GroupSection noReadMe={false} header="Economic and Social Council" link = "/meet/ac/ECOSOC" text={null} image={ECOSOC} />
    <GroupSection noReadMe={false} header="Security Council" link = "/meet/ac/SC" text={"The Security Council allows delegates to debate solutions for conflicts such as wars, revolutions, and other threats to international peace. Delegates in the security council are constantly being challenged with having to come up with strong and rigorous points while also trying to come to compromises with their country’s biggest rivals. Keeping this in mind is crucial as all of the P5 must agree for a clause to be passed, which is no easy task. Joining the Security Council means putting your skills to the test and elevating your MUN abilities to the next level. We are excited to see you all at ALSMUNⅠⅠ!"} image={SC} />
    <GroupSection noReadMe={false} header="Junior Committee" link = "/meet/ac/JC" text={"The Junior Committee is where the new generation of bright delegates debate the oppressing world issues of our day, discussing important general topics ranging from human rights issues to problems involving the environment. Here, in the junior committee, delegates begin their MUN journeys, taking their first steps in the world of diplomacy, where they’ll first learn the art of debating, how to write resolutions, and how to stand on a podium and confidently speak and express themselves in front of others. Here they’ll get their first taste of what it truly means to be a delegate in the United Nations, and the procedures involved when deciding actions required to solve world issues. These delegates must be ready to learn new skills and adapt, to be resilient, as with entering anything new or unknown they are likely to make mistakes. However, learning from them will ultimately help shape them into future leaders."} image={JC} />
</main>