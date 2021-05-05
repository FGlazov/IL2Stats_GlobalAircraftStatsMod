class BackgroundJob:
    """Abstract class which represents a job to be done in the background in stats.cmd while there is no new mission
    to be processed. This includes fixing corrupted data due to bugs, and retroactively computing aircraft stats, as
    well as filling in missing fields which were added in an update to the aircraft stats system.
    """

    def query_find_sorties(self, tour_cutoff):
        """
        Finds the sorties which need to be worked on.

        @param tour_cutoff The first tour that should be searched.
        @returns A django QuerySet which will find all the Sorties which need to be processed for this job.
        """
        print("[mod_stats_by_aircraft]: WARNING: Programing Error unimplemented background job query find.")

    def compute_for_sortie(self, sortie):
        """
        Does the necessary computations on a single sortie found by query_find_sorties.

        @param sortie Sortie as found by query_find_sorties.
        """
        print("[mod_stats_by_aircraft]: WARNING: Programing Error unimplemented background job one sortie.")

    def log_update(self, to_compute):
        """
        Message which shows a status update on how many sorties left to compute for this job.
        Printed to stats.cmd output.

        @param to_compute Nr of sorties found by compute_for_sortie method.
        """
        return "[mod_stats_by_aircraft]: WARNING: Programming error, unimplemented logs starting method."

    def log_done(self):
        """
        Message shown when this job is done. Printed to stats.cmd output.
        """

        return "[mod_stats_by_aircraft]: WARNING: Programming error, unimplemented logs done method."

    def reset_relevant_fields(self):
        """
        Optional method.

        This is a job done before any new sortie is processed. Used in corrupted data fixing background jobs which have
        to make sure that data is reset before a new mission is processed in, so that the relevant fields in new mission
        are at least correct.
        """
        pass