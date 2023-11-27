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
    <GroupSection header="International Court of Justice" link="/meet/ac/ICJ" text={null} image={ICJ} />
    <GroupSection header="Human Rights Council" link="/meet/ac/HRC" text={null} image={HRC} />
    <GroupSection header="General Assembly" link = "/meet/ac/GA" text={null} image={GA} />
    <GroupSection header="Economic and Social Council" link = "/meet/ac/ECOSOC" text={null} image={ECOSOC} />
    <GroupSection header="Security Council" link = "/meet/ac/SC" text={null} image={SC} />
    <GroupSection header="Junior Committee" link = "/meet/ac/JC" text={null} image={JC} />
</main>