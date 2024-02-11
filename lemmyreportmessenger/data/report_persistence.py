from lemmyreportmessenger.data.base import session_scope, Report
from lemmyreportmessenger.data import ContentType


class ReportPersistence:

    def acknowledge_report(self, report_id: int, report_type: ContentType, community_id: int):
        with session_scope() as session:
            session.add(
                Report(
                    report_id=report_id,
                    report_type=report_type,
                    community_id=community_id
                )
            )

    def has_been_acknowledged(self, report_id: int, report_type: ContentType) -> bool:
        with session_scope() as session:
            report = (session.execute(Report)
                      .filter(Report.report_id == report_id and Report.report_type == report_type)) \
                .scalar_one_or_none()

            return report is not None
